#!/usr/bin/env python3
"""
This module merge to xml files into one. First it checks if its sha's are the same to avoid merging of different projects an finally merge it into one called merged.xml.
"""

import sys
import argparse
from lxml import etree
import met.xmlMerger as merger

USAGE = './met-merger firstXml.xml secondXml.xml'

parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    usage=USAGE)

parser.add_argument('firstXml', help=argparse.SUPPRESS)
parser.add_argument('secondXml', help=argparse.SUPPRESS)


def main(args=None):

    opts = parser.parse_args(args)
    if not (opts.firstXml.endswith('.xml') and opts.secondXml.endswith(".xml")):
        print("Wrong extension!\nUsage: " + USAGE)

    else:
        xmlOne = sys.argv[1]
        xmlTwo = sys.argv[2]

        xml_doc_one = etree.parse(xmlOne)
        xml_doc_two = etree.parse(xmlTwo)

        rootOne = xml_doc_one.getroot()
        rootTwo = xml_doc_two.getroot()

        firstSha = rootOne.find('res').text
        secondSha = rootTwo.find('res').text

        secondArtefacts = rootTwo.find('data')

        merger.checkSha(firstSha, secondSha)
        merger.mergeFiles(rootOne, rootTwo, secondArtefacts)


if __name__ == '__main__':
    main()
