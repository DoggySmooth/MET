#!/usr/bin/env python3
"""
This module merges two xml files into one checking its "res" tag to verify if the two to be merged files are the same project.
"""
import jinja2
import json
import argparse

USAGE = './met-report.py jsonFile'

parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    usage=USAGE)
parser.add_argument('jsonFile', help=argparse.SUPPRESS)


def main(args=None):

    templateLoader = jinja2.FileSystemLoader(searchpath="../../res/template/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "template.html"
    template = templateEnv.get_template(TEMPLATE_FILE)

    opts = parser.parse_args(args)
    if not opts.jsonFile.endswith('.json'):
        print("Wrong extension!")

    else:
        j = json.load(open(opts.jsonFile))
        ressource = j['analysis']['res']
        artefacts = j['analysis']['data']['art']
        metas = j['analysis']['metadata']

        if isinstance(artefacts, dict):
            artefacts = [artefacts]
        if isinstance(metas, dict):
            metas = [metas]

        lenMetas = len(metas)

        outputText = template.render(
            ressource=ressource,
            lenMetas=lenMetas,
            metas=metas,
            artefacts=artefacts
        )  # this is where to put args to the template renderer
        print(outputText)


if __name__ == '__main__':
    main()
