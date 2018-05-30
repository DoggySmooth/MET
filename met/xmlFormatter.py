#!/usr/bin/env python3
"""
Pretty prints an XML file.
"""

import os
from lxml import etree


def formatXML(xml, parser):

    xmldoc = etree.parse(xml, parser)
    os.remove(xml)
    xmldoc.write(xml, encoding="utf-8", pretty_print=True)
