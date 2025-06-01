def addDigits(num):
    while(num>=10):
        sum_digits=0
        while(num>0):
            sum_digits+=num%10
            num=num//10
        num=sum_digits
    return num
num=int(input())
print(addDigits(num))quit
        
