import json


def test_validate():

    with open("tests/res/test_case2.json") as f:
        json.loads(f.read())
