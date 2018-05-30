#!/usr/bin/env python3
"""
This module opens an json file and extract the dataset ['art'], artefacts. See template
It checks if there is just one artefact, if yes it converts the dict into a list for easy processing. Finally it generate the graph as svg based on the dataset.
"""

import re
import graphviz as gv


def generateGraph(artefacts):
    """
    This function takes the artefacts dataset and creates it dot file as rendering an svg image
    """
    g = gv.Graph(format='svg')
    g.format = 'svg'
    regex = r"(.*)\/"
    subst = ""

    pkgs = {}
    files = {}
    whats = {}
    g.node('packages', shape='square')

    for artefact in artefacts:

        where = artefact['loc']
        what = artefact['type']
        name = artefact['name']
        level = artefact['level']

        match = re.match(regex, where)
        result = re.sub(regex, subst, where, 0, re.MULTILINE)

        packageName = match.group(1)
        if 'malicious' in level:
            color = 'red'
        else:
            color = 'yellow'

        if packageName not in pkgs:

            pkgs[packageName] = ''
            g.node(packageName)
            g.edge('packages', packageName)
            g.node("file" + packageName, "file")
            g.edge(packageName, "file" + packageName)

        if where not in files:
            files[where] = ""
            g.node(result + packageName, result)
            g.edge("file" + packageName, result + packageName)

        if what + result not in whats:
            whats[what + result] = ""
            g.node(what + result, what)
            g.edge(result + packageName, what + result)

        g.node(name + result, name, style="filled", fillcolor=color)
        g.edge(what + result, name + result)

    return g
