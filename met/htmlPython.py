#!/usr/bin/env python3
"""
This module create a html page to make it easy to read for the user.
"""


def firstpart(htmlFile):
    # First part of the html page
    with open("res/html/top.html") as top:
        htmlFile.write(top.read())


# Function that generates the content of the web page based on the JSON file
def generateHTML(metas, artefacts, sha256, htmlFile):
    i = 0
    htmlFile.write('<div class="box-header"><a> Metas </a></div>')
    for infos in metas:
        i += 1
        date = infos['date']
        access = infos['access']
        accessloc = infos['accessloc']
        author = infos['author']
        email = infos['email']
        permission = infos['perm']
        tags = infos['tags'].split(',')

        htmlFile.write('<div class="box-header"><a> Author ' + str(author) +
                       ' with index ' + str(i) + ' </a></div>')
        htmlFile.write(
            '<div class="meta-body" id="authorContent" ><table summary="Author Content">'
        )

        htmlFile.write(
            "<table><tr><td>Date</td><td>access</td><td>access location</td><td>email</td><td>permission</td></tr><tr><td>" + date + "</td><td> " + access + "</td><td> " + accessloc + " </td><td> " + email + "</td><td> " + permission + "</td></tr></table>")
        htmlFile.write(
            '<div class="box-header"><a>Malware Tags</a></div><table><tr>')
        for items in tags:
            htmlFile.write("<td>" + items + "</td>")
        htmlFile.write("</tr></table>")

    htmlFile.write('<div class="box-header"><a> Analysis </a></div>')
    htmlFile.write('<div class="box-header"><a> Artefacts: ' + str(sha256) +
                   '.apk</a></div>')

    for artefact in artefacts:
        where = artefact['loc']
        what = artefact['type']
        name = artefact['name']
        level = artefact['level']
        descr = artefact['desc']

        htmlFile.write(
            '<div class="box-body" id="artefactsContent" ><table summary="Artefacts Content">'
        )
        htmlFile.write(
            '<tr><td><b>Where</b></td><td><b>What</b></td><td><b>Name</b></td><td><b>Level</b></td></tr>'
        )
        htmlFile.write('<tr><td>' + where + '</td><td>' + what + '</td><td>' +
                       name + '</td><td>' + level + '</td></tr></table>')
        htmlFile.write('<table><tr><td style="width: 100%;">' + descr +
                       '</td></tr>')
        htmlFile.write('</table></div>')
