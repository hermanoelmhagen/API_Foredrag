import requests as r
import pprint
import sys
import xml.etree.ElementTree as ET

from os import environ
from sseclient import SSEClient
from time import sleep
from dotenv import load_dotenv

load_dotenv()

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
        print("\nSomething went wrong :(\n")

        
def streaming_demo(filename):

    xml_parsing(filename)
    
    with open(filename) as xml:
        response = r.post(URL, data=xml.read(), headers=headers).json()
        SSE_URL = response["RESPONSE"]["RESULT"][0]["INFO"]["SSEURL"]

    messages = SSEClient(SSE_URL)

    for msg in messages:
        print(msg)
        sleep(0.05)

        
def static_demo(filename):
    
    xml_parsing(filename)
    
    with open(XML_FILE) as xml:
        response = r.post(URL, data=xml.read(), headers=headers).json()
        
    pprint.pprint(response)

    
def xml_parsing(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    root[0].set("authenticationkey", environ["API_KEY"])
    tree.write(filename)

    
if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1].lower() == "-static" or sys.argv[1].lower() == "-streaming"):
        main(sys.argv[1])
    else:
        print(f"\nApply following argument(s): -static or -streaming\n\nExample (remove quotes): \n\t'python {sys.argv[0]} -static'\n\t'python {sys.argv[0]} -streaming'")
