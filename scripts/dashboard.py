#!/usr/bin/env python

import pandas as pd
from conversion import read_cases
from configparser import ConfigParser
from os.path import isfile, isdir, islink, basename, join as pjoin, abspath, dirname
from os import listdir, stat, getpid, getcwd, makedirs, umask
from shutil import rmtree
from time import ctime
from pwd import getpwuid
from subprocess import Popen, check_call, check_output
import numpy as np
import argparse
from subprocess import check_call
import re


SCRIPTDIR= dirname(abspath(__file__))

KB= 1024
MB= KB*KB
GB= MB*KB

# header importance
primary= 2
secondary= 3
tertiary= 4


def human_size(total_size):
    
    total_size= np.int64(total_size)

    if total_size >= GB:
        total_size= np.round(total_size / GB, decimals=2)
        total_size= str(total_size)+'G'
    elif total_size >= MB:
        total_size= np.round(total_size / MB, decimals=2)
        total_size= str(total_size)+'M'
    else:
        total_size= np.round(total_size / KB, decimals=2)
        total_size= str(total_size)+'K'

    return total_size


def getFolderSize(folder):

    total_size = 0.
    for item in listdir(folder):
        itempath = pjoin(folder, item)

        if isfile(itempath):
            total_size += stat(itempath, follow_symlinks=False).st_size

        elif isdir(itempath) and not islink(itempath):
            total_size += getFolderSize(itempath)

    return total_size


def getDetails(cases, item):

    details = pd.DataFrame(columns=['caseid', 'attribute_name', 'created_by', 'size_M', 'date_modified'])
    row = 0
    for id in cases:
        target = item.replace('$', id)

        try:
            if isfile(target):
                stat_obj = stat(target)
                details.loc[row] = [id, basename(target), getpwuid(stat_obj.st_uid).pw_name,
                                    np.round(stat_obj.st_size / MB, decimals=2), ctime(stat_obj.st_mtime)]

            elif isdir(target) and listdir(target):
                stat_obj = stat(target)
                total_size = getFolderSize(target)
                details.loc[row] = [id, basename(target), getpwuid(stat_obj.st_uid).pw_name,
                                    np.round(total_size / MB, decimals=2), ctime(stat_obj.st_mtime)]

            else:
                details.loc[row] = [id, basename(target), '-', '-', '-']

        except KeyError:
            pass

        row += 1
    

    # NOTE disable the total size calculation, it is already available in the summary
    total_size= sum([x for x in details['size_M'] if x!='-'])

    # multipy by MB to make --block-size=1
    total_size= human_size(total_size * MB)
    details.loc[row]= ['Total','','',total_size,'']

    return details


def getSummary(section, cases):

    summary = pd.DataFrame(columns=['item', f'exists\n(out of {len(cases)})', 'total size'])
    row= 0
    total_size= 0
    for key, item in section.items():

        count = 0
        for id in cases:
            target = item.replace('$', id)
            if isfile(target) or (isdir(target) and listdir(target)):
                count += 1
        
        # -L flag could be used to follow symlinks
        size= check_output('du -bcs {} | grep total'.format(item.replace('$','*')), shell= True).decode('UTF-8').split()[0]
        size= human_size(size)
        summary.loc[row]= [key, count, size]
        
        row += 1
        
        unit= eval(size[-1]+'B')
        value= float(size[:-1])
        total_size+= value*unit
    
    total_size= human_size(total_size)
    summary.loc[row]= ['Total','',total_size]


    return summary


def generateReport(configFile, tocFile, statFile, treeFile):
      
    directory= dirname(statFile)
    
    config= ConfigParser()
    config.optionxform= str
    config.read(configFile)

    cases= read_cases(config['CASELIST']['caselist'])


    ## summary

    # raw data
    df= getSummary(config['RAW'], cases)
    df.index+= 1
    df_html= df.to_html()
    header= 'Summary of given data'
    writeTableOfContents(tocFile, header)
    writeHeader(statFile, primary, header)
    writePlainHtml(statFile, df_html)
    

    # derivatives
    df= getSummary(config['DERIVATIVES'], cases)
    df.index+= 1
    df_html= df.to_html()
    header= 'Summary of derivatives'
    writeTableOfContents(tocFile, header)
    writeHeader(statFile, primary, header)
    writePlainHtml(statFile, df_html)
    


    ## details

    # raw data
    header= 'Details of given data'
    writeTableOfContents(tocFile, header)
    writeHeader(statFile, primary, header)
    writePlainHtml(tocFile, '<ul>')
    for key, item in config['RAW'].items():
        df = getDetails(cases, item)
        header= f'given-{key}-details'
        csvFile= pjoin(directory, f'{header}.csv')
        csvHtml= pjoin(directory, f'{header}.html')
        df.to_csv(csvFile, index= False)
        p= Popen(' '.join([pjoin(SCRIPTDIR, 'generateTable.R'), csvFile, csvHtml]), shell= True)
        p.wait()        
        
        modify_df_title(csvHtml, header)
        writeTableOfContents(tocFile, header, key)
        writeHeader(statFile, secondary, header, f'Item: {key}')
        writeCsvLink(statFile, csvFile, csvHtml)
    writePlainHtml(tocFile, '</ul>')
    
    
    # derivatives
    header= 'Details of derivatives'
    writeTableOfContents(tocFile, header)
    writeHeader(statFile, primary, header)
    writePlainHtml(tocFile, '<ul>')
    for key, item in config['DERIVATIVES'].items():
        df = getDetails(cases, item)
        header= f'derived-{key}-details'
        csvFile= pjoin(directory, f'{header}.csv')
        csvHtml= pjoin(directory, f'{header}.html')
        df.to_csv(csvFile, index= False)
        p= Popen(' '.join([pjoin(SCRIPTDIR, 'generateTable.R'), csvFile, csvHtml]), shell= True)
        p.wait()        
        
        modify_df_title(csvHtml, header)
        writeTableOfContents(tocFile, header, key)
        writeHeader(statFile, secondary, header, f'Item: {key}')
        writeCsvLink(statFile, csvFile, csvHtml)
    writePlainHtml(tocFile, '</ul>')

    
    header= 'Subject directory trees'
    writeTableOfContents(tocFile, header)
    writeHeader(statFile, primary, header)
    depth= config['TREE']['level']
    writePlainHtml(tocFile, '<ul>')
    
    # given
    header= 'Raw data trees'
    writeTableOfContents(tocFile, header)
    ref= writeHeader(statFile, secondary, header)
    writePlainHtml(statFile, f"""<p><a href="{basename(treeFile)}#{ref}">See trees</a></p>""")
    writeHeader(treeFile, secondary, header)
    givenDir= config['DIR']['givenDir']
    for id in cases:
        subDir= givenDir.replace('$', id)
        tree= check_output(f'tree {subDir} -L {depth}', shell=True)
        
        writePopDown(treeFile, id, tree.decode('UTF-8'))
    
    
    # derivatives
    header= 'Derived data trees'
    writeTableOfContents(tocFile, header)
    ref= writeHeader(statFile, secondary, header)
    writePlainHtml(statFile, f"""<p><a href="{basename(treeFile)}#{ref}">See trees</a></p>""")
    writeHeader(treeFile, secondary, header)
    derivDir= config['DIR']['derivDir']
    for id in cases:
        subDir= derivDir.replace('$', id)
        tree= check_output(f'tree {subDir} -L {depth}', shell=True)
        
        writePopDown(treeFile, id, tree.decode('UTF-8'))
    writePlainHtml(tocFile, '</ul>')

        
def modify_df_title(csvHtml, header):
    
    cmd= f"sed -i \"s+<title>datatables</title>+<title>{header}</title>+g\" {csvHtml}"
    check_output(cmd, shell=True)
    
    
def writePopDown(html, caseid, text, mode='a'):

    with open(html, mode) as f:
        message = f"""<details><summary>{caseid}</summary>
<p>
{text}
</p>
</details>"""

        f.write(message)


def writePlainHtml(html, text, mode= 'a'):

    with open(html, mode) as f:
        f.write(text)
    

def writeCsvLink(html, csvFile, csvHtml, mode='a'):

    with open(html, mode) as f:
        message = f"""
<a href="{basename(csvHtml)}">{basename(csvFile)}</a>"""

        f.write(message)

    
def writeHeader(html, serial, header, desc=None, mode='a'):
    
    if desc is None:
        desc= header
        
    with open(html, mode) as f:
        ref= ('-').join(header.split())
        message = f"""
<h{serial} id="{ref}">{desc}</h{serial}>"""

        f.write(message)

    return ref
        

def writeTableOfContents(html, header, desc=None, mode='a'):
    
    if desc is None:
        desc= header
        
    with open(html, mode) as f:
        ref= ('-').join(header.split())
        message = f"""
<li><a href=#{ref}>{desc}</a></li>"""

        f.write(message)



if __name__=='__main__':
    
    CWD= getcwd()
    
    parser = argparse.ArgumentParser(description='A lightweight dashboard for monitoring project progress \nSee details at https://github.com/pnlbwh/dashboard',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('outDir', type= str, default= f'report-PID', nargs='?',
        help= 'output directory for report files, default PWD/%(default)s')
    parser.add_argument('--dash-config', type= str, default= 'dash_config.ini',
        help= 'config file for generating dashboard, default PWD/%(default)s')
    parser.add_argument('--pipe-config', type= str,
        help= 'optional, config file for the pipeline \nSee examples at https://github.com/pnlbwh/luigi-pnlpipe/tree/master/params')
        
    args = parser.parse_args()        
        
    dashConfigFile= abspath(args.dash_config)
    if not isfile(dashConfigFile):
        raise FileNotFoundError(f'{dashConfigFile} could not be found, provide a valid --dash-config')
    pipeConfigFile= abspath(args.pipe_config) if args.pipe_config else None
    outDir= abspath(args.outDir.replace('PID', str(getpid())))
    
    if isdir(outDir):
        rmtree(outDir)
    makedirs(outDir, 0o755)
    
    outputFile= pjoin(outDir,'dashboard.html')
    tocFile= pjoin(outDir,'toc.html')
    statFile= pjoin(outDir,'stat.html')
    treeFile= pjoin(outDir,'tree.html')
    
    
    # initialize tocFile
    text=f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<link rel="stylesheet" href="css/common.css">
<link rel="stylesheet" href="css/dashboard.css">
<font size="+1"></font>
<title>Project overview</title>
</head>
<body>
<img src="https://raw.githubusercontent.com/pnlbwh/dashboard/master/docs/pnl-bwh-hms.png" />
<p><a href=https://github.com/pnlbwh/dashboard>https://github.com/pnlbwh/dashboard</a> is a lightweight dashboard for monitoring project progress</p>
<p>Developed by Tashrif Billah and Sylvain Bouix, Brigham and Women's Hospital (Harvard Medical School)</p>
<br>
_TIME_
<br>
<h{primary}>Table of Contents</h{primary}>
<p><ul>"""
    writePlainHtml(tocFile, text, 'w')
    
    
    # initialize statFile
    text=''
    writePlainHtml(statFile, text, 'w')
    
    
    # initialize treeFile
    text="""<!DOCTYPE html>
<html>
<head>
<title>Directory trees</title>
<meta charset="utf-8" />
<link rel="stylesheet" href="css/common.css">
<link rel="stylesheet" href="css/tree.css">
</head>
<body>
<span>"""
    writePlainHtml(treeFile, text, 'w')
    
        
    header= 'Dashboard configuration'
    writeTableOfContents(tocFile, header)
    with open(dashConfigFile) as f:
        writeHeader(statFile, primary, header)
        writePlainHtml(statFile, f"""
<span>
    <p id="dash-config">{f.read()}</p>
</span>
""")
    
    
    if pipeConfigFile:
        header= 'Pipeline configuration'
        writeTableOfContents(tocFile, header)
        with open(pipeConfigFile) as f:
            writeHeader(statFile, primary, header)
            writePlainHtml(statFile, f"""
<span>
    <p>{f.read()}</p>
</span>
""")
    
    
    generateReport(dashConfigFile, tocFile, statFile, treeFile)

    
    writePlainHtml(tocFile, '</ul>')
    writePlainHtml(treeFile, """
</span></body></html>""")
    
    with open(tocFile) as f:
        toc= f.read()    
    with open(statFile) as f:
        stat= f.read()
    with open(outputFile, 'w') as f:
        toc= re.sub('_TIME_', f'<p><b>* This report was generated on {ctime()}</b></p>', toc)
        f.write(toc+stat)
        f.write('</body></html>')
    
    check_call(f'cp -a {SCRIPTDIR}/../css {outDir}', shell=True)
    check_call(f'chmod -R 755 {outDir}', shell= True)



