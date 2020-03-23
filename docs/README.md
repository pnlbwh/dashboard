![](pnl-bwh-hms.png)

https://github.com/pnlbwh/dashboard is a lightweight dashboard for monitoring project progress

Developed by Tashrif Billah and Sylvain Bouix, Brigham and Women's Hospital (Harvard Medical School)

See example dashboard at https://pnlbwh.github.io/dashboard/report/dashboard.html

Table of Contents
=================
    
   * [Requirements](#requirements)
      * [Python](#python)
      * [R](#r)
   * [Configuration](#configuration)
      * [Dashboard](#dashboard)
      * [Pipeline](#pipeline)
   * [Usage](#usage)
   * [Examples](#examples)

Table of Contents created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)


# Requirements

The following libraries are required:

## Python

* pandas

## R

* DT


# Configuration

## Dashboard

See [dash_config.ini](../scripts/dash_config.ini) and edit according to your file/directory paths.

## Pipeline

See https://github.com/pnlbwh/luigi-pnlpipe/tree/master/params . This configuration file 
is optional. If you provide it, then it will be printed in the dashboard.



# Usage

> scripts/dashboard.py -h

```bash
usage: dashboard.py [-h] [--dash-config DASH_CONFIG]
                    [--pipe-config PIPE_CONFIG]
                    [outDir]

A lightweight dashboard for monitoring project progress
See details at https://github.com/pnlbwh/dashboard

positional arguments:
  outDir                output directory for report files, default PWD/report-PID

optional arguments:
  -h, --help            show this help message and exit
  --dash-config DASH_CONFIG
                        config file for generating dashboard, default PWD/dash_config.ini
  --pipe-config PIPE_CONFIG
                        optional, config file for the pipeline
                        See examples at https://github.com/pnlbwh/luigi-pnlpipe/tree/master/params
```


# Examples

```bash
# dash_config.ini exists in the PWD, writes to default outDir, --pipe-config unavailable
scripts/dashboard.py

# dash_config.ini exists in the PWD, writes to provided outDir, --pipe-config unavailable
scripts/dashboard.py /tmp/report

# dash_config.ini exists in the PWD, writes to provided outDir, --pipe-config available
scripts/dashboard.py /tmp/report --pipe-config ~/luigi-pnlpipe/params/struct_pipe_params.cfg

# dash_config.ini does not exist in the PWD, writes to provided outDir, --pipe-config available
scripts/dashboard.py /tmp/report --dash-config /path/to/config.ini --pipe-config ~/luigi-pnlpipe/params/struct_pipe_params.cfg
```





