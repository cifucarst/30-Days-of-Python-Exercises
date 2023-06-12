#Write your code here
class Calculator:
    def power(self,n,p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return pow(n,p)
            
# class Calculator:
#     def power(self, base, exponent):
#         if base < 0 or exponent < 0:
#             raise Exception("Base and exponent should be non-negative")
        
#         return pow(base, exponent)
    
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   