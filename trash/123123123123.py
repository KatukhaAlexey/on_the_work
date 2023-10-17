number = int(input())
n1 = number // 1000 % 10
n2 = number // 100 % 10
n3 = number // 10 % 10
n4 = number % 10
new_number = (number // 1000 % 10) * 100 + (number // 100 % 10) * 1000 + (number // 10 % 10) + (number % 10) * 10
print(new_number)