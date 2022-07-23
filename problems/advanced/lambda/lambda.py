"""
Function lambda
"""

list_lambda = [
    ['value1', 5],
    ['value3', 11],
    ['value2', 100],
    ['value4', 8]
]
print("Product name")
print(sorted(list, key=lambda i: i[0], reverse=True))
print("Product key")
print(sorted(list, key=lambda i: i[1], reverse=True))
