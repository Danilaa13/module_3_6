data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]



def calculate_structure_sum(age):
    total_sum = 0

    if isinstance(age, (int, float)):
        total_sum += age
    elif isinstance(age, str):
        total_sum += len(age)
    elif isinstance(age, (list, tuple, set)):
        for i in age:
            total_sum += calculate_structure_sum(i)
    elif isinstance(age, dict):
        for key, value in age.items():

            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)

    return total_sum

result = calculate_structure_sum(data_structure)

print(result)