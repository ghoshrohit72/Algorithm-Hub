N = int(input())
numbers = list()
counts = list()

for i in range(0,N):
    numbers.append(input())

q = int(input())
for i in range(0,q):
    checkString = input()
    count = 0
    for num in numbers:
        if num == checkString:
            count=count+1
    counts.append(count)

for count in counts:
    print(count)