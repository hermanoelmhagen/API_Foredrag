import requests as r
from sseclient import SSEClient
from time import sleep
import pprint
import sys

URL = "https://api.trafikinfo.trafikverket.se/v2/data.json"

XML_FILE = "demo.xml"
XML_FILE_STREAMING = "demo_streaming.xml"

headers = {'Content-Type':'text/xml'}


def main(argv):
    if argv.lower() == "-static":
        static_demo(XML_FILE)
    
    elif argv.lower() == "-streaming":
        streaming_demo(XML_FILE_STREAMING)

    else:
        print(f"\nApply following argument(s): -static or -streaming\n\nExample (remove quotes): \n\t'python {sys.argv[0]} -static'\n\t'python {sys.argv[0]} -streaming'")

def streaming_demo(filename):

    with open(filename) as xml:
        response = r.post(URL, data=xml.read(), headers=headers).json()
        SSE_URL = response["RESPONSE"]["RESULT"][0]["INFO"]["SSEURL"]

    messages = SSEClient(SSE_URL)

    for msg in messages:
        print(msg)
        sleep(0.05)


def static_demo(filename):
    
    with open(XML_FILE) as xml:
        response = r.post(URL, data=xml.read(), headers=headers).json()
        
    pprint.pprint(response)

    
if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(f"\nApply following argument(s): -static or -streaming\n\nExample (remove quotes): \n\t'python {sys.argv[0]} -static'\n\t'python {sys.argv[0]} -streaming'")