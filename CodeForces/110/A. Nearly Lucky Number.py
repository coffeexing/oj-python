def is_lucky_number(number: int):
    count = 0
    num = number
    while num > 0:
        digit = num % 10
        num = num // 10
        if digit == 4 or digit == 7:
            count += 1

    return count, count == len(str(number))
#
#
# n = int(input())
# cnt, _ = is_lucky_number(n)
# cnt, flag = is_lucky_number(cnt)
#
# if flag:
#     print("YES")
# else:
#     print("NO")


# concise

def count_lucky_digits(n):
    return str(n).count('4') + str(n).count('7')

def is_lucky(n):
    return n > 0 and all(d in '47' for d in str(n))

n = int(input())
lucky_count = count_lucky_digits(n)

if is_lucky(lucky_count):
    print("YES")
else:
    print("NO")