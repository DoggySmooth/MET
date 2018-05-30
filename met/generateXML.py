#!/usr/bin/env python3
"""
This module checks the args of the function for correct input. It validates the XML and finally write it in an file.
"""
import re
from lxml import etree


# Check if the arguments are passed correctly
def checkArgs(plim, xml):
    """
    This function checks if the args have the correct extension.
    """
    regex = r".*\."
    resultPlim = re.sub(regex, "", plim)
    resultXml = re.sub(regex, "", xml)

    if resultPlim != 'plim':
        raise ValueError(
            '\n\nWrong arguments has been passed to the script!\nThis happens if there are multiple plim files in smaef directory\n'
        )

    if resultXml != 'xml':
        raise ValueError('Second argument has to be an .xml extension')


# Validates XML schema based on an SCHEMA
def validateXML(xml):
    """
    This function validates the XML file based on the schema
    """
    xmlschema_doc = etree.parse("../../res/schema/s2extend")
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml)
    result = xmlschema.validate(xml_doc)

    return result


# Writes a formatted XML file to the temporary file
def writeXML(xml):

    xml_doc = etree.parse(xml)
    file = open("tmp.xml", "w")
    xml_doc.write("tmp.xml", encoding="utf-8", pretty_print=True)
    file.close()
