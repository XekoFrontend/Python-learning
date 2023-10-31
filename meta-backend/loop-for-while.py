color = ['red', 'yellow', 'blue', 'green']


for i in color:
    print('My color is: ', i, end=" | ")


count = 0

while count < len(color):
    print('My color is: ', count, color[count])
    count += 1


for i in range(10):
    for j in range(10):
        print(j, end=" ❤️  ")

    print()


num_list = [33, 42, 5, 66, 77, 22, 16, 79,
            36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

count = 0

for x, num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)

print(count)
