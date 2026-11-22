import pytest

from nasq_core.errors import (
    PROBLEM_CONTENT_TYPE,
    NasqError,
    ServiceNotReadyError,
    code_for_status,
    problem_document,
)
from nasq_core.messages import MESSAGES


def test_problem_content_type_is_rfc7807() -> None:
    assert PROBLEM_CONTENT_TYPE == "application/problem+json"


def test_problem_document_has_rfc7807_members_and_nasq_extensions() -> None:
    doc = problem_document(
        code="not_found",
        status=404,
        locale="en",
        instance="/missing",
        request_id="req-12345678",
    )

    assert doc["type"] == "urn:nasq:problem:not_found"
    assert doc["title"] == MESSAGES["not_found"]["en"].title
    assert doc["detail"] == MESSAGES["not_found"]["en"].detail
    assert doc["status"] == 404
    assert doc["instance"] == "/missing"
    assert doc["code"] == "not_found"
    assert doc["request_id"] == "req-12345678"


def test_problem_document_is_translated_to_arabic() -> None:
    doc = problem_document(code="not_found", status=404, locale="ar", instance=None, request_id=None)

    assert doc["title"] == MESSAGES["not_found"]["ar"].title


def test_problem_extensions_cannot_overwrite_standard_members() -> None:
    with pytest.raises(ValueError, match="status"):
        problem_document(
            code="internal_error",
            status=500,
            locale="en",
            instance=None,
            request_id=None,
            extensions={"status": 200},
        )


def test_nasq_error_carries_code_status_and_extensions() -> None:
    error = ServiceNotReadyError(extensions={"checks": {"database": "unavailable"}})

    assert isinstance(error, NasqError)
    assert error.code == "service_not_ready"
    assert error.status == 503
    assert error.extensions == {"checks": {"database": "unavailable"}}


def test_every_nasq_error_code_has_a_message() -> None:
    for cls in (NasqError, ServiceNotReadyError):
        assert cls.code in MESSAGES


@pytest.mark.parametrize(
    ("status", "code"),
    [
        (404, "not_found"),
        (405, "method_not_allowed"),
        (422, "validation_failed"),
        (500, "internal_error"),
        (503, "service_not_ready"),
        (418, "http_error"),
    ],
)
def test_code_for_status(status: int, code: str) -> None:
    assert code_for_status(status) == code
    assert code in MESSAGES
