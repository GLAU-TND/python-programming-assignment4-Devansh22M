prefix = input()
strings = eval(input())
result = [i for i in strings if i[:len(prefix)] == prefix]
print(result)