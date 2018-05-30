import met.generateGraph as graph
import json


def test_graph():

    output = open("tests/res/Graph.gv")
    output = output.read().strip()

    j = json.load(open("tests/res/test_case.json"))

    artefacts = j['analysis']['data']['art']

    if isinstance(artefacts, dict):
        artefacts = [artefacts]

    g = graph.generateGraph(artefacts)
    g = str(g).strip()

    assert g == output
