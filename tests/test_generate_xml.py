import os
import met.generateXML as xm


def test_generateXML():

    target = open("tests/res/test_case3.xml")
    os.system("met/scripts/compile.py tests/res/test_case.plim > aaa.xml")
    result = open("aaa.xml")

    target = target.read().replace(" ", "")
    result = result.read().replace("\n", "")
    result = result.replace(" ", "")
    target = target.strip()
    result = result.strip()

    assert target == result


def test_validate():

    xml = open("tests/res/test_case.xml")
    assert xm.validateXML(xml)
