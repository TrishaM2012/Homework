test_dictionary = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print("Test dictionary:", test_dictionary)

value = str(input("Enter the value you want to check the frequency of: "))

frequency = list(test_dictionary.values()).count(value)
print(f"The frequency of the value {value} is: {frequency}")