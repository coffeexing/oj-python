a = input()
b = input()
num_a = int(a, 2)
num_b = int(b, 2)
result = num_a ^ num_b
print(bin(result)[2:].zfill(len(a)))
