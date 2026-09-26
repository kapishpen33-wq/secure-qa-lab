import json
from pathlib import Path

from app.result_analyzer import summarize_results


DATA_PATH = Path("test_data/test_results.json")


def main():
    try:
        with DATA_PATH.open(encoding="utf-8") as file:
            payload = json.load(file)

        suite_name = payload["suite_name"]
        results = payload["results"]

        summary = summarize_results(results)

        print(f"Suite: {suite_name}")
        print(f"Total tests: {summary['total']}")
        print(f"Pass rate: {summary['pass_rate']:.2f}%")
        print()

        for status, count in summary["counts"].items():
            print(f"{status}: {count}")

    except FileNotFoundError:
        print(f"ERROR: File not found: {DATA_PATH}")

    except json.JSONDecodeError:
        print(f"ERROR: Invalid JSON in {DATA_PATH}")

    except KeyError as error:
        print(f"ERROR: Missing required field: {error}")

    except (TypeError, ValueError) as error:
        print(f"ERROR: {error}")


if __name__ == "__main__":
    main()
