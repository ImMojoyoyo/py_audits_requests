#Libraries

import requests
import argparse


parser = argparse.ArgumentParser(description="Request headers from website")
parser.add_argument("-t", "--target", help="Objective")
parser = parser.parse_args()

def _requestHeaders():
    if parser.target:
        print(parser.target)
        try:
            url = requests.get(url=parser.target)
            #print(url.headers) -> This line show our project like a dictionry
            header = dict(url.headers)
            for h in header:
                print(h + " : " + header[h])
        except:
            print("We didn't find the link")
    else:
        print("We have not objective!")



def main():
    _requestHeaders()

if __name__ == "__main__" :
        main()