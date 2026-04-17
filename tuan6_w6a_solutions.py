import ast
import sys


def parse_int_list(line: str) -> list[int]:
    line = line.strip()
    return list(map(int, line.split())) if line else []


def parse_tuple(line: str) -> tuple[int, ...]:
    line = line.strip()
    if not line:
        return ()
    if line.startswith("(") and line.endswith(")"):
        return tuple(ast.literal_eval(line))
    return tuple(map(int, line.split()))


def parse_dict_literal(line: str) -> dict:
    line = line.strip()
    if not line:
        return {}
    return ast.literal_eval(line)


def parse_kv_pairs(line: str) -> dict[str, list]:
    result: dict[str, list] = {}
    for token in line.split():
        if ":" not in token:
            continue
        key, value = token.split(":", 1)
        if value.lstrip("-+").isdigit():
            try:
                value_parsed = int(value)
            except ValueError:
                value_parsed = value
        else:
            value_parsed = value
        result.setdefault(key, []).append(value_parsed)
    return result


def w6a1() -> None:
    numbers = parse_int_list(input())
    seen = set()
    result = []
    for n in numbers:
        if n not in seen:
            seen.add(n)
            result.append(n)
    print(result)


def w6a2() -> None:
    numbers = parse_int_list(input())
    result = []
    current = 0
    for n in numbers:
        current += n
        result.append(current)
    print(result)


def w6a3() -> None:
    values = parse_tuple(input())
    try:
        k = int(input().strip())
    except ValueError:
        k = 0
    if not values:
        print(())
        return
    k = k % len(values)
    rotated = values[k:] + values[:k]
    print(tuple(rotated))


def w6a4() -> None:
    pairs_line = input()
    result = parse_kv_pairs(pairs_line)
    print(result)


def w6a5() -> None:
    numbers = parse_int_list(input())
    result = {
        "positives": sum(1 for x in numbers if x > 0),
        "negatives": sum(1 for x in numbers if x < 0),
        "zeros": sum(1 for x in numbers if x == 0),
    }
    print(result)


def w6a6() -> None:
    numbers = parse_int_list(input())
    print(sum(numbers))


def w6a7() -> None:
    values = parse_tuple(input())
    if not values:
        print()
        return
    first = values[0]
    last = values[-1]
    reversed_tuple = tuple(reversed(values))
    print(first)
    print(last)
    print(reversed_tuple)


def w6a8() -> None:
    items = input().split()
    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    print(counts)


def w6a9() -> None:
    dict1 = parse_dict_literal(input())
    dict2 = parse_dict_literal(input())
    merged: dict = {}
    for key in sorted(set(dict1) | set(dict2)):
        if key in dict1 and key in dict2:
            merged[key] = dict1[key] + dict2[key]
        elif key in dict1:
            merged[key] = dict1[key]
        else:
            merged[key] = dict2[key]
    print(merged)


def w6a10() -> None:
    numbers = parse_int_list(input())
    try:
        k = int(input().strip())
    except ValueError:
        k = 0
    found = set()
    result = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == k:
                pair = (numbers[i], numbers[j])
                if pair not in found:
                    found.add(pair)
                    result.append(pair)
    result.sort(key=lambda x: (x[0], x[1]))
    print(result)


def w6a11() -> None:
    values = parse_tuple(input())
    evens = tuple(x for x in values if x % 2 == 0)
    odds = tuple(x for x in values if x % 2 != 0)
    print(evens)
    print(odds)


def w6a12() -> None:
    numbers = parse_int_list(input())
    if not numbers:
        print()
        return
    counts: dict[int, int] = {}
    for n in numbers:
        counts[n] = counts.get(n, 0) + 1
    max_count = max(counts.values())
    candidates = [n for n, c in counts.items() if c == max_count]
    print(min(candidates))


def w6a13() -> None:
    original = parse_dict_literal(input())
    reversed_dict = {value: key for key, value in original.items()}
    print(reversed_dict)


def w6a14() -> None:
    list1 = parse_int_list(input())
    list2 = parse_int_list(input())
    set2 = set(list2)
    seen = set()
    result = []
    for x in list1:
        if x in set2 and x not in seen:
            seen.add(x)
            result.append(x)
    print(result)


def w6a15() -> None:
    original = parse_dict_literal(input())
    try:
        k = int(input().strip())
    except ValueError:
        k = 0
    filtered = {key: value for key, value in original.items() if isinstance(value, int) and value > k}
    print(filtered)


TASKS = {
    "1": w6a1,
    "2": w6a2,
    "3": w6a3,
    "4": w6a4,
    "5": w6a5,
    "6": w6a6,
    "7": w6a7,
    "8": w6a8,
    "9": w6a9,
    "10": w6a10,
    "11": w6a11,
    "12": w6a12,
    "13": w6a13,
    "14": w6a14,
    "15": w6a15,
}


if __name__ == "__main__":
    if len(sys.argv) > 1:
        task_number = sys.argv[1]
    else:
        task_number = input().strip()

    if task_number in TASKS:
        TASKS[task_number]()
    else:
        print("Please enter a task number from 1 to 15.")
