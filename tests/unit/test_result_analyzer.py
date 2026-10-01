import pytest

from app.result_analyzer import (calculate_pass_rate, count_statuses, summarize_results, validate_results)
VALID_RESULTS = ["PASS","FAIL","PASS", "BLOCKED", "FAIL", "PASS", "SKIPPED"]

def test_count_statuses_repeated_results():
    actual = count_statuses(VALID_RESULTS)
    expected = {"PASS":3, "FAIL":2, "BLOCKED":1, "SKIPPED":1}

    assert actual == expected

def test_calculate_pass_rate_rounds_to_two_decimals():
    actual = calculate_pass_rate(VALID_RESULTS)
    expected = 42.86

    assert actual == expected

def test_summarize_results_returns_complete_sumamry():
    actual = summarize_results(VALID_RESULTS)
    expected = {
        "total":7, 
        "counts":{"PASS":3, "FAIL":2, "BLOCKED":1, "SKIPPED":1}, 
        "pass_rate":42.86}
    assert actual == expected

def test_calculate_pass_rate_returns_zero_for_empty_list():
    actual = calculate_pass_rate([])
    assert actual == 0.0

def test_validate_results_rejects_non_list():
    with pytest.raises(TypeError, match = 'list'):
        validate_results("PASS")

def test_validate_results_rejects_non_string():
    with pytest.raises(TypeError, match="string"):
        validate_results(["PASS", 500])

def test_validate_results_rejects_unsupported_status():
    with pytest.raises(ValueError, match="Invalid status"):
        validate_results(["PASS", "UNKNOWN"])

def test_count_statuses_does_not_modify_input():
    results = ["PASS", "FAIL", "PASS"]
    original_results = results.copy()
    count_statuses(results)

    assert results == original_results