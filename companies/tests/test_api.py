import json
from unittest import TestCase
from django.test import Client
from django.urls import reverse
import pytest
from companies.models import Companies


@pytest.mark.django_db
class BasicCompanyApiTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.companies_url = reverse("companies-list")

    def tearDown(self) -> None:
        pass


@pytest.mark.django_db
class TestGetCompanies(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.companies_url = reverse("companies-list")

    def tearDown(self) -> None:
        pass

    def test_zero_companies_should_return_empty_list(self) -> None:
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_one_company_exists_should_succeed(self) -> None:
        test_company = Companies.objects.create(name="Apple")
        response = self.client.get(self.companies_url)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data[0]["name"], test_company.name)
        self.assertEqual(response_data[0]["status"], "Hiring")
        self.assertEqual(response_data[0]["application_link"], "")
        self.assertEqual(response_data[0]["notes"], "")
        test_company.delete()


class TestPostCompany(BasicCompanyApiTestCase):
    def test_create_company_without_arguments_should_fail(self) -> None:
        response = self.client.post(path=self.companies_url)
        self.assertEqual(response.status_code, 400)

    def test_create_existing_company_should_fail(self) -> None:
        Companies.objects.create(name="Apple")
        response = self.client.post(path=self.companies_url, data={"name": "Apple"})
        # self.assertEqual(response.status_code,400)
        # self.assertEqual(json.loads(response.content),{'name':['Companies with this name allready exist']},)

    def test_create_company_with_only_all_field_should_be_default(self) -> None:
        response = self.client.post(
            path=self.companies_url, data={"name": "test company name"}
        )
        self.assertEqual(response.status_code, 201)

        response_data = json.loads(response.content)
        self.assertEqual(response_data["status"], "Hiring")
        self.assertEqual(response_data["application_link"], "")
        self.assertEqual(response_data["notes"], "")

    def test_create_company_with_layoffs_status_should_succeed(self) -> None:
        response = self.client.post(
            path=self.companies_url,
            data={"name": "tesdt company name", "status": "Layoff"},
        )
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.content)
        self.assertEqual(response_data.get("status"), "Layoff")

    def test_create_company_with_wrong_status_should_fail(self) -> None:
        response = self.client.post(
            path=self.companies_url, data={"name": "test company name", "status": "s"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("s", str(response.content))
        # self.assertIn("",str(response.content))

    @pytest.mark.xfail
    def test_should_be_ok_if_fails(self) -> None:
        self.assertEqual(1, 2)

    @pytest.mark.skip
    def test_should_be_skkiped(self) -> None:
        self.assertEqual(1, 2)


def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")
    # pass


def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)


import logging

logger = logging.getLogger("CORONA_LOGS")


def fanction_that_logs_something() -> None:
    try:
        raise ValueError("CoronaVirus Exception")
    except ValueError as e:
        logger.warning(f"I am logging {str(e)}")


def test_logged_warning_level(caplog) -> None:
    fanction_that_logs_something()
    assert "I am logging CoronaVirus Exception" in caplog.text


def test_logged_info_level(caplog) -> None:
    with caplog.at_level(logging.INFO):
        logger.info("I am logging info level")
        assert "I am logging info level" in caplog.text
