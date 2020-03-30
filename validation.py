import random
import string

def randomPassword():
    """Generate a random password """
    randomSource = string.ascii_letters 
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_uppercase)

    passwordList = list(password)
    password = ''.join(passwordList)
    return password



details=[]

no=0
counter=1
while no<counter:
    i=str(counter)
    x=input("Enter First Name of User "+i+" : ")
    y=input("Enter Last Name of User "+i+": ")
    p=input("Enter Email of User "+i+": ")
    z=randomPassword()
    b=z
    f=x
    g=y
    twoletter=f[:2]
    lastTwoletter=g[-2:].lower()
    k=twoletter+b+lastTwoletter
    

    
    print("Password:- ",k)
    
    report = input("Do like this password[Y/N]: ")
    if report=='y' or report=='Y':
        details.append((x,y,p,k))
        print("User ",i,"details:- (First Name: ", x,", Second Name: ",y,", Email: ",p,", password: ",k,")")
    if report=='n' or report=='N':
        while True:
            k=input("Enter new password: ")
            if len(k) < 7: 
                print("Input less than 7")
                continue
            else:
                
                break
        details.append((x,y,p,k))
        print("User ",i,"details:- (First Name: ", x,", Second Name: ",y,", Email: ",p,", password: ",k,")")
        
        
        
   
    report2=input("Do you want to create another user[Y/N]: ")
    
    if report2=='y' or report2=='Y':
        counter+=1

    if report2=='n' or report2=='N':
        no=1000
for x, y,p,k in details:
    print(p,"-(First Name: ", x,", Second Name: ",y,", Email: ",p,", password: ",k,")")       
    