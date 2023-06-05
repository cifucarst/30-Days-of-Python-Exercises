# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_book = {}

for _ in range(n):
    a = input().split()
    phone_book[a[0]] = a[1]
    
for _ in range(n):
    b = input()
    if b not in phone_book:
        print("Not found")
    else:
        print("{}={}".format(b, phone_book[b]))