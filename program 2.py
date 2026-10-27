data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

print("Training Data:")

for row in data:
    print(row)

print("\nPositive Examples:")

for row in data:
    if row[-1] == 'Yes':
        print(row)

print("\nNegative Examples:")

for row in data:
    if row[-1] == 'No':
        print(row)