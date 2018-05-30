#!/usr/bin/env python3
"""
This module merge to xml files into one. First it checks if its sha's are the same to avoid merging of different projects an finally merge it into one called merged.xml.
"""

import sys
from lxml import etree


def checkSha(firstSha, secondSha):
    """
    This function checks if the two files that are to be merged have the same res
    """

    if firstSha != secondSha:
        raise ValueError('\n\nCan\'t merge files!\nSha are different!')
    return True


def mergeFiles(rootOne, rootTwo, secondArtefacts):
    """
    This function takes the xmltree and merge the differences.
    """

    for artefact in rootOne[-1]:
        flag = True
        for arte in rootTwo[-1]:
            if artefact.find('name').text == arte.find(
                    'name').text and artefact.find('loc').text == arte.find(
                        'loc').text and artefact.find(
                            'type').text == arte.find('type').text:
                flag = False
                break
        if flag:
            child = etree.SubElement(secondArtefacts, "art")

            etree.SubElement(child, "loc")
            child.find('loc').text = artefact.find('loc').text
            etree.SubElement(child, "type")
            child.find('type').text = artefact.find('type').text
            etree.SubElement(child, "name")
            child.find('name').text = artefact.find('name').text
            etree.SubElement(child, "level")
            child.find('level').text = artefact.find('level').text
            etree.SubElement(child, "desc")
            child.find('desc').text = artefact.find('desc').text

    my_tree = etree.ElementTree(rootTwo)

    with open('./merged.xml', 'wb') as f:
        f.write(etree.tostring(my_tree, pretty_print=True))
    f.close()


def main(args=None):

    xmlOne = sys.argv[1]
    xmlTwo = sys.argv[2]

    xml_doc_one = etree.parse(xmlOne)
    xml_doc_two = etree.parse(xmlTwo)

    rootOne = xml_doc_one.getroot()
    rootTwo = xml_doc_two.getroot()

    firstSha = rootOne.find('res').text
    secondSha = rootTwo.find('res').text

    secondArtefacts = rootTwo.find('data')

    checkSha(firstSha, secondSha)
    mergeFiles(rootOne, rootTwo, secondArtefacts)


if __name__ == '__main__':
    main()
