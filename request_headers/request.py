#Libraries

import requests
import argparse


parser = argparse.ArgumentParser(description="Request headers from website")
parser.add_argument("-t", "--target", help="Objective")
parser = parser.parse_args()

def _requestHeaders():
    if parser.target:
        print(parser.target)
    else:
        print("We have not objective!")



def main():
    _requestHeaders()

if __name__ == "__main__" :
        main()