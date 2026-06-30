for i in range(1,11):
    if i%2==0:
        print(i,end=' ')
 
print("\n")




def is_prime(n):

    if n<=1:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True


print(is_prime(1))
print(is_prime(2))
print(is_prime(7))
print(is_prime(10))
print(is_prime(13))
print(is_prime(25))
print(is_prime(29))
print("\n")





def check_even_odd(n):
    if n%2==0:
        return 'Even'
    
    return 'Odd'



print(check_even_odd(0))
print(check_even_odd(1))
print(check_even_odd(4))
print(check_even_odd(7))
print(check_even_odd(12))
print(check_even_odd(15))
print(check_even_odd(22))
print(check_even_odd(33))
print("\n")



def is_palindrome(text):
    text=text.lower()
    text=text.replace(' ','')
    
    tet=text[::-1]

    if tet==text:
        return True
    
    return False

print(is_palindrome('madam'))
print(is_palindrome('hello'))
print(is_palindrome('racecar'))
print(is_palindrome('python'))
print(is_palindrome('level'))
print(is_palindrome('A man a plan a canal Panama'))
print('\n')

class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def describe(self):
        print('name:',self.name)
        print('age:',self.age)

     
    def breathe(self):
        print(f'{self.name} is breathing....')


class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed=breed

    def describe(self):
        print('name:',self.name)
        print('age:',self.age)
        print('breed:',self.breed)

    def speak(self):
        print('woof!')


class Cat(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color

    def describe(self):
        print('name:',self.name)
        print('age:',self.age)
        print('color:',self.color)

    def speak(self):
        print('meow!')


dog1 = Dog("Tommy", 3, "Labrador")
cat1 = Cat("Kitty", 2, "White")




print("DOG DETAILS")
dog1.describe()
dog1.speak()
dog1.breathe()
print("CAT DETAILS")
cat1.describe()
cat1.speak()
cat1.breathe()



