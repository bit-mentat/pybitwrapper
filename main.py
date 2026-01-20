import pretty_json as pj
import requests
from decimal import Decimal
import json
import sys
from pathlib import Path
import parse
sys.path.append(str(Path(__file__).resolve().parents[1]))
import vars   


args = {"jsonrpc":"1.0","id":"pybitwrapper"}
auth = (vars.user, vars.password)

while True:
    try:
        cmd = input("bitcoin-cli>")
        test = cmd.split(" ")

        args["method"] = test[0]

        if len(test) > 1:
            args["params"] = [parse.parse_arg(p) for p in test[1:]]
        else:
            args["params"] = []

        r = requests.post(vars.url, auth=auth, json=args, timeout=10)
        
        obj = json.loads(r.text, parse_float=Decimal)
        print(pj.pretty_json(obj, indent=2))
    except EOFError:
        print("\nExiting")
        break
		