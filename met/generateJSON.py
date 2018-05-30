#!/usr/bin/env python3
"""
This module generates a JSON file out of the xml. Validate the JSON format and finally pretty print it.
"""


import os
import json


def generateJSON(xml, jsonName):
    """
    This function takes an xml and jsonName to generate the xmlfile.
    """
    # Generates an unformatted JSON file from an XML file stripping unwanted strings
    os.system("met/xml2json.py -t xml2json -o " + jsonName + " " + xml +
              " --strip_text")


def validateJSON(jsonName):
    """
    This function validates the json format and prettyprint it.
    """

    # Checks if the format of the JSON file is valide
    with open(jsonName) as f:
        json.loads(f.read())
        print("JSON is valid!")
    # Format JSON file for a better overview
    os.system("python -m json.tool " + jsonName + " > tmp.json")
