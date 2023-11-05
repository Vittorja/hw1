x = int(input("Please enter a five digit number "))
num_1 = x % 10
num_2 = ((x // 10) % 10)
num_3 = ((x // 100) % 10)
num_4 = ((x // 1000) % 10)
num_5 = (x // 10000)
num_result = (num_1 * 10000 + num_2 * 1000 + num_3 * 100 + num_4 * 10 + num_5)
print(num_result)
