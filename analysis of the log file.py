import sys
from collections import defaultdict

# Логи як список рядків
log_data = [
    "2024-01-22 08:30:01 INFO User logged in successfully.",
    "2024-01-22 08:45:23 DEBUG Attempting to connect to the database.",
    "2024-01-22 09:00:45 ERROR Database connection failed.",
    "2024-01-22 09:15:10 INFO Data export completed.",
    "2024-01-22 10:30:55 WARNING Disk usage above 80%.",
    "2024-01-22 11:05:00 DEBUG Starting data backup process.",
    "2024-01-22 11:30:15 ERROR Backup process failed.",
    "2024-01-22 12:00:00 INFO User logged out.",
    "2024-01-22 12:45:05 DEBUG Checking system health.",
    "2024-01-22 13:30:30 INFO Scheduled maintenance."
]


def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)  # Розділяємо рядок на частини
    if len(parts) < 4:
        return None  # Якщо рядок не містить всіх частин, повертаємо None
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }


def load_logs(logs: list) -> list:
    parsed_logs = []
    for line in logs:
        parsed_line = parse_log_line(line.strip())
        if parsed_line:
            parsed_logs.append(parsed_line)
    return parsed_logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].upper() == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count}")


def main(level=None):
    logs = load_logs(log_data)  # Завантажуємо логи з списку
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"No logs found for level: {level}")


if __name__ == "__main__":
    # Задайте рівень логування, якщо потрібно
    main()
    main('ERROR')
