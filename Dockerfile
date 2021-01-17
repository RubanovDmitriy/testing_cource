FROM python:3.8.5

# WORKDIR /code

ADD requirements.txt .

RUN python -m pip install -r requirements.txt

COPY 03_api_testing/ ./03_api_testing

CMD pytest -v ./03_api_testing
