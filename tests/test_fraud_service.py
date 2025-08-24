import pytest
from app.fraud_service import FraudService


@pytest.fixture
def service():
    return FraudService()


def test_high_amount_is_fraud(service):
    tx = {"amount": 10000, "country": "US", "user_age": 30}
    assert service.is_fraudulent(tx) is True


def test_safe_transaction(service):
    tx = {"amount": 50, "country": "US", "user_age": 30}
    assert service.is_fraudulent(tx) is False


def test_foreign_country_flags(service):
    tx = {"amount": 100, "country": "RU", "user_age": 30}
    assert service.is_fraudulent(tx) is True


def test_young_user_only_is_not_enough(service):
    tx = {"amount": 100, "country": "US", "user_age": 18}
    assert service.is_fraudulent(tx) is False
