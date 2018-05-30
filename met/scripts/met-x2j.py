#!/usr/bin/env python3
"""
This module compiles the plim file checking the xml format with xsd.
"""
import argparse
import xmltodict
import json

USAGE = './met-x2j example.xml'

parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    usage=USAGE)
parser.add_argument('xmlFile', help=argparse.SUPPRESS)


def main(args=None):

    opts = parser.parse_args(args)
    if not opts.xmlFile.endswith('.xml'):
        print("Wrong Extension")
    else:
        xml = opts.xmlFile
        with open(xml) as fd:
            doc = xmltodict.parse(fd.read())
        print(json.dumps(doc))


if __name__ == '__main__':
    main()
