import pytest
import requests
import validators
from jsonschema import validate
from urllib.parse import urljoin

DOMAIN = 'https://api.openbrewerydb.org/'


@pytest.mark.parametrize('url, status_code',
                         [
                             ('breweries', 200),
                             ('breweries/5494', 200),
                             ('https://api.openbrewerydb.org/breweries/search?query=dog', 200),
                             ('https://api.openbrewerydb.org/breweries/autocomplete?query=dog', 200),
                         ])
def test_url_status(url, status_code):
    res = requests.get(urljoin(DOMAIN, url))
    assert res.status_code == status_code


def test_api_json_schema():
    res = requests.get(urljoin(DOMAIN, 'breweries/5494'))

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "brewery_type": {"type": "string"},
            "street": {"type": "string"},
            "address_2": {"type": "null"},
            "address_3": {"type": "null"},
            "city": {"type": "string"},
            "county_province": {"type": "null"},
            "state": {"type": "string"},
            "postal_code": {"type": "string"},
            "country": {"type": "string"},
            "longitude": {"type": "string"},
            "latitude": {"type": "string"},
            "phone": {"type": "string"},
            "website_url": {"type": "string"},
            "updated_at": {"type": "string"},
            "created_at": {"type": "string"}
        }
    }

    validate(instance=res.json(), schema=schema)


@pytest.mark.parametrize('url, number',
                         [
                             ('breweries', 20),
                             ('breweries?per_page=1', 1),
                             ('breweries?per_page=11', 11),
                             ('breweries?per_page=33', 33),
                             # Max per page is 50
                             ('breweries?per_page=99', 50),
                         ])
def test_len_page(url, number):
    res = requests.get(urljoin(DOMAIN, url))
    res_json = res.json()
    assert len(res_json) == number


def test_website_url_is_url():
    res = requests.get(urljoin(DOMAIN, 'breweries/5494'))
    assert validators.url(res.json()["website_url"])


def test_encoding():
    res = requests.get(urljoin(DOMAIN, 'breweries'))
    assert res.encoding == 'utf-8'


@pytest.mark.parametrize('header, header_status',
                         [
                             ('content-type', 'application/json; charset=utf-8'),
                             ('Content-Encoding', 'gzip'),
                             ('Server', 'cloudflare'),
                             ('Cache-Control', 'max-age=86400, public'),
                         ])
def test_headers(header, header_status):
    res = requests.get(urljoin(DOMAIN, 'breweries'))
    assert res.headers[header] == header_status

