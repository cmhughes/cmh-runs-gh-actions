#!/usr/bin/env python

import xml.etree.ElementTree as ET
import sys, os, re, logging, argparse, subprocess, zipfile, yaml, time, datetime

# argument parsing
#   reference: https://docs.python.org/3/howto/argparse.html#id1
parser = argparse.ArgumentParser()

parser.add_argument("filename", 
                    type=str, 
                    help="filename, should have .tex or .xml extension")

parser.add_argument("-a", "--sampleargument", 
                    type=str,choices=["info", "status", "debug","warning","error"],
                    default="status",
                    help="make4ht loglevel")

args = parser.parse_args()

# filename work
filename = args.filename
base_filename, file_extension = os.path.splitext(filename)
filename_aux_list = [base_filename + '.aux']
filename_log = base_filename + '.log'
filename_tex = base_filename + '.tex'
filename_html = base_filename + '.html'
filename_xml = base_filename + '.xml'

# create a logging mechanism (reference: https://docs.python.org/3/howto/logging.html)
logging.basicConfig(filename=filename_xml+'.log', 
                    level=logging.DEBUG,
                    format='%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M %p',
                    filemode='w')

print('hello world, argument '+args.sampleargument)
