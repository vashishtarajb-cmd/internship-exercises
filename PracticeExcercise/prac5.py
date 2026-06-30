
def sumofdigits(n):
    total=0
    while n>0 :
        a=n%10
        total=total+a
        n=n//10

    return total
    
print(sumofdigits(123))
print()

def factorial(k):
    fact=1
    for i in range(1,k+1):
        fact=fact*i
    return fact

print(factorial(5))
print()
s = input("Enter a string: ").lower()

for vowel in "aeiou":
    c = 0

    for ch in s:
        if ch == vowel:
            c += 1

    print(vowel, ":", c)
        
