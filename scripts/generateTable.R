#!/usr/bin/env Rscript

args = commandArgs(trailingOnly=TRUE)

library(DT)

df= read.csv(args[1])
table= datatable(df)
saveWidget(table, args[2], selfcontained= FALSE)


