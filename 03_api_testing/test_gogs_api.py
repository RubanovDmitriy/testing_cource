import requests
from jsonschema import validate


def test_url_status():
    r = requests.get('https://dog.ceo/api/breed/hound/images')
    assert r.status_code == 200


def test_api_json_schema():
    res = requests.get('https://dog.ceo/api/breed/hound/images')

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        }
    }

    validate(instance=res.json(), schema=schema)

def test_hound_afghan():
    pass
