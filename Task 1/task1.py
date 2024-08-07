israel: dict = {"name": "Israel", "birth": 1948, "population_millions": 9.3, "capital": "Jerusalem", "language": "Hebrew", "cities": {"Jerusalem", "Tel aviv", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod"}, "currency": "ILS", "area_kilometer": 22145, "gdp_billion": 450}

#Task a
print(f"The capital city is: {israel.get('capital')}")

#Task b
print(f"All the keys of the dict is: {israel.keys()}")

#Task c
bigkletter: list[str] = [i.upper() for i in israel.keys()]
print(bigkletter)

#Task d
print(f"The values of israel dict are: {israel.values()}")

#Task e
lenofv: list[str] = [len(str(value)) for value in israel.values()]
print(lenofv)

#Task f
print(f"f. {israel.items()}")

#Task g
newisrael: dict = israel.copy()

#Task h
newisrael.clear()

#Task i
newisrael2: dict = dict.fromkeys(israel)

#Task j
del israel["currency"]

#Task k
print(israel.pop("area_kilometer"))

#Task l
israel.update({"national_sport": "Soccer", "population_millions": 9.4})

