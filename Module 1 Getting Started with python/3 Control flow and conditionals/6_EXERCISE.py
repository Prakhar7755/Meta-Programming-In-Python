num_list = [33, 42, 5, 66, 77, 22, 16, 79,
            36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

for i in num_list:
    if i > 45:
        print("Over 45")
    else:
        print("Under 45")


for index, num in enumerate(num_list):
    if num == 36:
        print('Number found at position:', index)


count = 0

for num in num_list:
    count += 1

print("Count:", count)

count = 0

for x, num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)
        break

print(count)
