#!/usr/bin/env python3
"""
Generates a Graph from a jsonFile.


Example: ./met-graph example.json
"""

import json
import sys
import argparse
import met.generateGraph as gen

USAGE = './met-graph jsonFile'

parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    usage=USAGE)
parser.add_argument('jsonFile', help=argparse.SUPPRESS)


def main(args=None):

    opts = parser.parse_args(args)
    if not opts.jsonFile.endswith('.json'):
        print("Wrong extension!")
    else:
        jsonFile = opts.jsonFile
        j = json.load(open(jsonFile))

        artefacts = j['analysis']['data']['art']

        assert len(
            sys.argv) % 2 == 0, "All operations must be paired with a file."
        if isinstance(artefacts, dict):
            artefacts = [artefacts]

        g = gen.generateGraph(artefacts)
        g.render()
        print("Graph generated successfully")


if __name__ == '__main__':
    main()
