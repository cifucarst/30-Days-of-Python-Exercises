# Enter your code here. Read input from STDIN. Print output to STDOUT
number = int(input())

for i in range(number):
    string = input()
    even = ""
    odd = ""
    for j in range(len(string)):
        if j % 2 == 0:
            even += string[j]
        else:
            odd += string[j]
            
    print(f'{even} {odd}')
    