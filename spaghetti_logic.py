from typing import Iterable


TAX_MULTIPLIER = 1.15
LOG_FILE_PATH = "log.txt"


def calculate_total(amount: float) -> float:
    return amount * TAX_MULTIPLIER


def format_total_message(total: float) -> str:
    return f"Total: {total:.2f}"


def append_results_log(results: list[float], file_path: str = LOG_FILE_PATH) -> None:
    with open(file_path, "a") as log_file:
        log_file.write(f"{results}\n")


def process_data(data: Iterable[float]) -> list[float]:
    results: list[float] = []

    for amount in data:
        total = calculate_total(amount)
        print(format_total_message(total))
        results.append(total)

    append_results_log(results)
    return results
