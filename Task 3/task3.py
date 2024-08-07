import statistics


def get_statistics(numbers: list[int]) -> dict:
    return {"sum": sum(numbers), "max number": max(numbers), "min number": min(numbers), "count:": len(numbers),
            "average": statistics.mean(numbers)}


print(get_statistics([1, 2, 3, 5, 7, 9]))
