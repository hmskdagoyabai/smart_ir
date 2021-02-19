import json
import argparse

json_path = "./config/val/val.json"

p = argparse.ArgumentParser()
p.add_argument("-n", "--name", help="CommandName", required=True)
args = p.parse_args()
name = args.name
try:
    f = open(json_path, "r")
    records = json.load(f)
    f.close()
except:
    records = {}

try:
    records.pop(name)
except:
    print(name + " is not exist")
    exit()

f = open(json_path, "w")
f.write(json.dumps(records).replace("],", "],\n")+"\n")
f.close()

print(name+" is Deleted")
