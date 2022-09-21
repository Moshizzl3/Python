from pathlib import Path
import argparse


p = argparse.ArgumentParser()
subparsers = p.add_subparsers()


option1_parser = subparsers.add_parser('createfolder')
option1_parser.add_argument('param1')
def createDir(args):
    p = Path(str(args.param1))
    try:
        p.mkdir()
    except FileExistsError as exc:
        print(exc)
option1_parser.set_defaults(func=createDir)

option2_parser = subparsers.add_parser('appendfile')
option2_parser.add_argument('param1')
option2_parser.add_argument('param2')

def appenToFile(args):
    filename = open(args.param1, "a+")
    filename.write(args.param2)
    filename.write("\n")
    filename.close()
option2_parser.set_defaults(func=appenToFile)

option3_parser = subparsers.add_parser('readfile')
option3_parser.add_argument('param1')
def readFile(args):
    filename = open(args.param1, "r")
    print(filename.read())
    filename.close()
option3_parser.set_defaults(func=readFile)


args = p.parse_args()
args.func(args)




