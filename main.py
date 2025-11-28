import pretty_json as pj
import requests
from decimal import Decimal
import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
import vars   


args = {"jsonrpc":"1.0","id":"pybitwrapper"}
auth = (vars.user, vars.password)

while True:
    cmd = input("bitcoin-cli>")
    test = cmd.split(" ")

    args["method"] = test[0]
    args["params"] = [test[1]]


    r = requests.post(vars.url, auth=auth, json=args, timeout=10)
    
    obj = json.loads(r.text, parse_float=Decimal)
    print(pj.pretty_json(obj, indent=2))
		