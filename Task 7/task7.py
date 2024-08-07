countries = [{'name': 'Israel', 'population': 9.3, 'birth': 1948},
{'name': 'United States', 'population': 331.9, 'birth': 1776}, {'name': 'Japan',
'population': 125.8, 'birth': 660 }, {'name': 'Australia', 'population': 25.7, 'birth': 1901},
{'name': 'Canada', 'population': 38.0, 'birth': 1867}]

# Task 1
morethan30: list[str] = list(filter(lambda x: x.get("population") > 30, countries))
# Task 2
after1800: list[str] = list(filter(lambda x: x.get("birth") > 1800, countries))
# Task 3
countname: list[int] = list(map(lambda x: x["name"], countries))
# Task 4
countbirth: list[int] = list(map(lambda x: x["birth"], countries))
# Task 5
print(list(sorted(countries, key=lambda b: b["birth"])))
# Task 6
print(list(sorted(countries, key=lambda p: p["population"])))