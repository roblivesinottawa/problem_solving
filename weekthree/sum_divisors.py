def sum_divisors(n):
    sum = 1
    div = 2
    if n == 0:
        return 0

    while div < (n / 2 + 1): # (36 / 2 + 1) = 19
        if n % div == 0:
            sum = sum + div
            # print(sum) # 3, 6, 10, 16, 25, 37, 55
        div += 1
        # print(div) # 19 

    return f"sum = {sum}"

print(sum_divisors(36))







# def sum_div(num):
#     add = []
#     total_sum = 0
#     for x in range(1, num - 1):
#         if num % x == 0:
#             add.append(str(x))
#             total_sum = total_sum + x
#             print(total_sum)

#     return f"{(add)} + {total_sum}"

# print(sum_div(36))

