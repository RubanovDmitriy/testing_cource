import pytest
import requests
import validators
from jsonschema import validate
from urllib.parse import urljoin

DOMAIN = 'https://dog.ceo/api/'


@pytest.mark.parametrize('url, status_code',
                         [
                             ('breed/hound/images', 200),
                             ('breeds/list/all', 200),
                             ('breeds/image/random', 200),
                             ('breed/hound/images', 200),
                             ('breed/hound/list', 200),
                         ])
def test_url_status(url, status_code):
    res = requests.get(urljoin(DOMAIN, url))
    assert res.status_code == status_code


def test_api_json_schema():
    res = requests.get(urljoin(DOMAIN, 'breed/hound/images'))

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        }
    }

    validate(instance=res.json(), schema=schema)


@pytest.mark.parametrize('url, number',
                         [
                             ('breed/hound/images/random/1', 1),
                             ('breed/hound/images/random/5', 5),
                             ('breed/hound/images/random/10', 10),
                             ('breed/hound/images/random/33', 33),
                             ('breed/hound/images/random/999', 999),
                         ])
def test_len_random_imgages(url, number):
    res = requests.get(urljoin(DOMAIN, url))
    images_list = res.json()["message"]
    assert len(images_list) == number


def test_images_are_urls():
    res = requests.get(urljoin(DOMAIN, 'breeds/image/random'))
    assert validators.url(res.json()["message"])


def test_encoding():
    res = requests.get(urljoin(DOMAIN, 'breeds/list/all'))
    assert res.encoding == 'utf-8'


@pytest.mark.parametrize('header, header_status',
                         [
                             ('content-type', 'application/json'),
                             ('Content-Encoding', 'gzip'),
                             ('Server', 'cloudflare'),
                             ('Cache-Control', 'max-age=1800'),
                         ])
def test_headers(header, header_status):
    res = requests.get(urljoin(DOMAIN, 'breeds/list/all'))
    assert res.headers[header] == header_status

