import sys, os
import requests
import subprocess
from pprint import pprint
import csv


def list_of_files(filetype):
    """
    Searches for files of type, and outputs list to a file
    """
    filetype_search = "." + filetype
    outfile = "files_" + filetype + ".txt"
    #print "outfile: ", outfile
    
    command = ("find ../class_lectures | grep {} > {}").format(filetype_search, outfile)
    #print command
    result = subprocess.check_output(command,shell=True)
    #return int(result.strip().split()[0])

#list_of_files("md")
list_of_files("ipynb")
list_of_files("pdf")



def write_links(filetype):
   
   #filein = open("files_ipynb.txt", "r")
   #fileout = open("links_ipynb.md", "w")
   filein = open("files_" + filetype + ".txt", "r")
   fileout = open("links_" + filetype + ".md", "w")
   linect = -1
   for line in filein:
       linect += 1
       if linect == 0:
           table_row1 = "| Week | Day | File | Line |"
           table_row2 = "|------|-----|------|------|"
           fileout.write(table_row1 + '\n')
           fileout.write(table_row2 + '\n')

       #print line
       line = line.rstrip('\n')
       filelink=line
       #print "line: ", line
       #print line
       items = line.split("/")
       #print items
       info_week = items[2]
       info_day = items[3]
       link = "[" + items[4] + "]" + "(" + filelink + ")"
       print
       #print info_week
       #print info_day
       #print link

       tableout = "| " + info_week + " | " + info_day + " | " + link + " | " + str(linect+1) + " |" 
       print tableout
       
       fileout.write(tableout + '\n')


write_links("ipynb")
write_links("pdf")
