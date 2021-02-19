import json
import argparse

p = argparse.ArgumentParser()
p.add_argument("-f", "--file", help="Filename",       required=True)
args = p.parse_args()
FILE = args.file
try:
    f = open(FILE, "r")
    records = json.load(f)
    f.close()
except:
    records = {}

keys = records.keys()
