word: str = input("Please enter a word: ")
oper: str = input("Please enter an operator name (lower,upper, len, reverse): ").lower()

oper_dict: dict = {"lower": lambda w: w.lower(),
                   "upper": lambda u: u.upper(),
                   "len": lambda l: len(l),
                   "reverse": lambda r: r[::-1]}

print(f"The word {word} with the operation {oper} is: {oper_dict[oper](word)}")