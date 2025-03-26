n=int(input())
sum=0
while(n):
    b=n%10
    sum=sum+b
    n=n//10
print(sum)