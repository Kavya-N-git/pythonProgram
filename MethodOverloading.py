#method overloading
#python donot support for method overloading because its dynamically typed language and we dont specify any type of data here 


class Myclass:
    def getinput(self,name=None,age=None):
        if name and age != None:
            print("hello",name)
            print("you are",age,"years old now\n")
        elif name != None and age == None:
            print("hello",name)
        else:
            print("hello")
            
obj=Myclass()
while True:
    print("1.to print both name and age\n2.to print only name\nto print only hello\n0.to exit\n")
    ch=int(input("enter your choice\n"))
    if ch == 1:
        name=input("enter name\n")
        while(1):
            if not(name):
                name=input("name field cannot be empty,enter name\n")
                continue
            elif name.isdigit():
                name=input("enter valid name\n")
                continue
            else:
                break
            
        age = input("enter age\n")
        while(1):
                if not(age):
                    age=input("age cannot be empty, enter age\n")
                    continue
                if age.isalpha():
                    age=input('enter only integers\n')
                    continue
                else:
                    break
        age=int(age)
        obj.getinput(name,age)
    elif ch == 2:
        name=input("enter name\n")
        while(1):
            if not(name):
                name=input("name field cannot be empty,enter name\n")
                continue
            elif name.isdigit():
                name=input("enter valid name\n")
                continue
            else:
                break
        obj.getinput(name)
    elif ch == 3:
        obj.getinput()
    else:
        break
    
