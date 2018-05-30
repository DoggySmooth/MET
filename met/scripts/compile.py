#!/usr/bin/env python3
"""
This module compiles the plim file checking the xml format with xsd.
"""
import os
import argparse
import met.generateXML as gen

USAGE = './met.py example.plim'

parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    usage=USAGE)
parser.add_argument('plimFile', help=argparse.SUPPRESS)


def main(args=None):

    # Initialize parser
    opts = parser.parse_args(args)
    if not opts.plimFile.endswith('.plim'):
        print("Wrong extension!")
    else:
        # Initialize variables for better overview
        plim = opts.plimFile
        xml = plim[:-5] + ".xml"

        # Generated an unformatted XML file from an PLIM file
        os.system("plimc " + plim + " > " + xml)
        result = gen.validateXML(xml)

        if result:
            gen.writeXML(xml)
            print(open("tmp.xml").read())
            os.remove(xml)
        else:
            print("XML Schema is invalid!")
            os.remove(xml)
            raise ValueError("Schema is invalid!")


if __name__ == '__main__':
    main()
