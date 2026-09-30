from app.result_analyzer import count_statuses

def test_count_statuses_counts_repeated_results():
    results = ["PASS", "FAIL", "PASS"]
    actual = count_statuses(results)

    assert actual == {"PASS":2, "FAIL":1}