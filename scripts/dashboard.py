#!/usr/bin/env python

import pandas as pd
from conversion import read_cases
from configparser import ConfigParser
from os.path import isfile, isdir, basename, join as pjoin
from os import listdir, stat, getpid
from time import ctime
from pwd import getpwuid
from subprocess import Popen, check_call
import numpy as np

KB= 1e3
MB= 1e6
GB= 1e9


def getFolderSize(folder):

    total_size = 0.
    for item in listdir(folder):
        itempath = pjoin(folder, item)

        if isfile(itempath):
            total_size += stat(itempath).st_size

        elif isdir(itempath):
            total_size += getFolderSize(itempath)

    return total_size


def getDetails(section, cases):

    details = pd.DataFrame(columns=['case ID', 'file name', 'user', 'size M', 'date modified'])
    row = 0
    for key, item in section.items():

        for id in cases:
            target = item.replace('id', id)

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
                details.loc[row] = [id, basename(target), 'x', 'x', 'x']

            row += 1

        details.loc[row] = ['.'] * 5
        row += 1


    return details


def getSummary(section, cases):
    summary = pd.DataFrame(index=['count'])
    for key, item in section.items():

        count = 0
        for id in cases:
            target = item.replace('id', id)
            if isfile(target) or (isdir(target) and listdir(target)):
                count += 1

        summary[key] = count


    return summary


def writeDataFrame(html, df, header, mode='a'):

    with open(html, mode) as f:
        message = f"""<html>
        <head></head>
        <body><p>{header}</p></body>
        </html>"""

        f.write(message)
        f.write(df)


def writePopDown(html, caseid, text, mode='a'):

    with open(html, mode) as f:
        message = f"""<br><br><details><summary>{caseid}</summary>
        <p>
        {text}
        </p>
        </details>"""

        f.write(message)


def writePlainHtml(html, text, mode= 'a'):

    with open(html, mode) as f:
        f.write(text)



def generateReport(configFile, outputFile):

    config= ConfigParser()
    config.read(configFile)

    cases= read_cases(config['CASELIST']['caselist'])


    ## summary

    # raw data
    df= getSummary(config['RAW'], cases)
    df_html= df.to_html()
    writeDataFrame(outputFile, df_html, 'Summary of given data','w')

    # derivatives
    df= getSummary(config['DERIVATIVES'], cases)
    df_html= df.to_html()
    writeDataFrame(outputFile, df_html, 'Summary of derivatives')



    ## details

    # raw data
    df = getDetails(config['RAW'], cases)
    df_html = df.to_html()
    writeDataFrame(outputFile, df_html, 'Details of given data')

    # derivatives
    df = getDetails(config['DERIVATIVES'], cases)
    df_html = df.to_html()
    writeDataFrame(outputFile, df_html, 'Details of derivatives')



    writePlainHtml(outputFile, '<meta charset="UTF-8">\n<span style="white-space: pre-wrap">\n')

    derivDir= config['DIR']['derivDir']
    for id in cases:
        subDir= derivDir.replace('id', id)
        treeFile= f'/tmp/tree-{getpid()}.txt'
        check_call(f'tree {subDir} -L 3 > {treeFile}', shell=True)

        with open(treeFile) as f:
            tree= f.read()

        writePopDown(outputFile, id, tree)

    writePlainHtml(outputFile, '</span>\n')


    #TODO we can define separate DataFrame for each key, such DataFrames can be hidden and expanded by clicking arrow




if __name__=='__main__':
    configFile= '/home/tb571/Downloads/INTRuST_BIDS/config.ini'
    outputFile= '/tmp/dashboard.html'


    generateReport(configFile, outputFile)

