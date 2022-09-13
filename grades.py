#Xion Lawson
#grades.py
#This will show the inputed student's first and last name, as well as their GPU, and determine if they are eligible for special treatment based on them.
lname=("test")
while(lname!="ZZZ"):
 lname=input("Input a student's last name, or input 'ZZZ' to cancel: ")
 fname=input("Input the student's first name: ")
 print("Input",fname,lname+"'s GPU.")
 intgpu=input()
 floatgpu=float(intgpu)
 if(floatgpu>=3.5):
  print(fname,lname+"GPU is",int(floatgpu),".This student will be added to the Dean's List.")
 elif(floatgpu>=3.25):
  print(fname,lname+"GPU is",int(floatgpu),".This student will be placed onto the Honor Roll.")
 else:
  print(fname,lname+"GPU is",int(floatgpu))
else:
    print("Good day.")
