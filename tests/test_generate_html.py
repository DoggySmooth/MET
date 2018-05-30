import met.htmlPython as py
import json


def test_generateHtml():

    ha = open("tests/res/htmlTest.txt")
    ha = ha.read().strip()

    j = json.load(open("tests/res/test_case.json"))

    htmlFile = open("aaa.html", "w")
    sha256 = j['analysis']['res']

    artefacts = j['analysis']['data']['art']
    metas = j['analysis']['metadata']

    py.generateHTML(metas, artefacts, sha256, htmlFile)
    htmlFile.close()

    htmlContent = open("aaa.html")

    assert htmlContent.read() == ha
