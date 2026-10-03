import pytest

from app.result_analyzer import (calculate_pass_rate, count_statuses, summarize_results, validate_results)
@pytest.fixture
def valid_results():
    return [
        "PASS",
        "FAIL",
        "PASS",
        "BLOCKED",
        "FAIL",
        "PASS",
        "SKIPPED"
    ]

def test_count_statuses_repeated_results(valid_results):
    actual = count_statuses(valid_results)
    expected = {"PASS":3, "FAIL":2, "BLOCKED":1, "SKIPPED":1}

    assert actual == expected

def test_summarize_results_returns_complete_sumamry(valid_results):
    actual = summarize_results(valid_results)
    expected = {
        "total":7, 
        "counts":{"PASS":3, "FAIL":2, "BLOCKED":1, "SKIPPED":1}, 
        "pass_rate":42.86}
    assert actual == expected

@pytest.mark.parametrize(
        ("results", "expected_rate"),
        [
            ([], 0.0),
            (["PASS"], 100.0),
            (["FAIL"], 0.0),
            (["PASS", "FAIL"], 50.0),
            (["PASS", "PASS", "FAIL"], 66.67)
        ],
        ids = [
            "empty",
            "all-pass",
            "no-pass",
            "half-pass",
            "rounded-rate"
        ]
)

def test_calculate_multiple_inputs_pass_rate(results, expected_rate):
    actual = calculate_pass_rate(results)
    assert actual == expected_rate

@pytest.mark.parametrize(
        "invalid_results",
        [
            "PASS",
            None,
            ("PASS","FAIL"),
        ],
        ids=[
            "string",
            "none",
            "tuple"
        ]
)

def test_validate_results_negative_testing(invalid_results):
    with pytest.raises(TypeError, match="list"):
        validate_results(invalid_results)

@pytest.mark.parametrize(
        "unsupported_status",
        [
            "UNKNOWN",
            "PASSED",
            "pass"
        ]
)

def test_validate_results_rejects_unsupported_status(unsupported_status):
    with pytest.raises(ValueError, match="Invalid status|unsupported_status"):
        validate_results(["PASS", unsupported_status])

def test_validate_results_rejects_non_string_item():
    with pytest.raises(TypeError, match="string"):
        validate_results(["PASS", 500])

def test_count_statuses_does_not_modify_input():
    results = ["PASS", "FAIL", "PASS"]
    original_results = results.copy()
    count_statuses(results)

    assert results == original_results