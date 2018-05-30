from lxml import etree
import met.xmlMerger as merger


def test_sha():

    xml_doc_one = etree.parse(open("tests/res/test_case2.xml"))
    xml_doc_two = etree.parse(open("tests/res/test_case.xml"))

    rootOne = xml_doc_one.getroot()
    rootTwo = xml_doc_two.getroot()

    firstSha = rootOne.find('res').text
    secondSha = rootTwo.find('res').text

    assert merger.checkSha(firstSha, secondSha)


def test_merge():

    xml_doc_one = etree.parse(open("tests/res/test_case2.xml"))
    xml_doc_two = etree.parse(open("tests/res/test_case.xml"))

    rootOne = xml_doc_one.getroot()
    rootTwo = xml_doc_two.getroot()

    secondArtefacts = rootTwo.find('data')

    merger.mergeFiles(rootOne, rootTwo, secondArtefacts)

    one = open("tests/res/merged.xml")
    two = open("./merged.xml")

    one = one.read().strip()
    two = two.read().strip()
    assert (one == two)
