!\[API Test Automation](https://github.com/mscottcomp-commits/senior-qa-api-testing-framework/actions/workflows/api-tests.yml/badge.svg)
# Senior QA API Testing Framework



This project is a Python-based API automation framework built with `pytest` and `requests`. It validates REST API behavior using positive tests, negative tests, JSON response checks, schema validation, response header validation, response time validation, and GitHub Actions CI/CD.



\## Project Purpose



The purpose of this project is to demonstrate API testing skills from a Senior QA Analyst perspective while expanding into automation. The framework focuses on validating API behavior, identifying response issues, and producing clear test results through HTML reports.



\## Tech Stack



\- Python

\- pytest

\- requests

\- pytest-html

\- jsonschema

\- GitHub Actions



\## API Under Test



This framework uses the public JSONPlaceholder API:



https://jsonplaceholder.typicode.com



\## Features



\- Reusable API client

\- Reusable assertion helpers

\- Centralized configuration file

\- Separated test data

\- JSON schema validation

\- Response header / Content-Type validation

\- Response time validation

\- Positive API tests

\- Negative API tests

\- Data-driven tests using pytest parametrize

\- Smoke and regression test markers

\- HTML test report generation

\- GitHub Actions CI/CD pipeline



\## Project Structure



```text

senior-qa-api-testing-framework/

│

├── .github/

│   └── workflows/

│       └── api-tests.yml

│

├── data/

│   └── test\_data.py

│

├── reports/

│

├── schemas/

│   └── post\_schema.py

│

├── tests/

│   ├── test\_create\_update\_delete\_post.py

│   └── test\_posts\_api.py

│

├── utils/

│   ├── api\_client.py

│   └── assertions.py

│

├── config.py

├── pytest.ini

├── requirements.txt

└── README.md

