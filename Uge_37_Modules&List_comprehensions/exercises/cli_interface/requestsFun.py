import requests
from pathlib import Path
import argparse
import subprocess
import os

p = argparse.ArgumentParser()
p.add_argument('param1')
p.add_argument('param2')


def getUrl(args):
    print("inde")
    response = requests.get(args.param1, allow_redirects=True)
    o = open('logo.html', 'wb')
    o.write(response.content)

    subprocess.run(['git', 'add', '-A'])
    subprocess.run(['git', 'commit', '-m', args.param2])
    subprocess.run(['git', 'status'])

    subprocess.run(['git', 'push'])



p.set_defaults(func=getUrl)

args = p.parse_args()
args.func(args)
