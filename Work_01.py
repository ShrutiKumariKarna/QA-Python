#Exercise 1:Ask user their username and greet them 
#Exercise 2:Ask user name 2 numbers and perform arithmetic operation 
#Exercise 3: Ask for name and print it 3 times using a for loop. 
#Exercise 4:Create a list name tests and include some tests within that list and loop through the list and print (“Testing for (testname)”) 
#Exercise 5: Ask for a number, print whether it is even or odd. 
#Exercise 6:Create a dictionary and  loop through them and print them. 
#Exercise 7: Ask for age. If age greater than or equals to  18 → print "You can vote" Else → print "You cannot vote" 
#Exercise 8:  Asks the user for their age If age < 10 → print "50% discount" Else → print "No discount 
#Exercise 9:Print “Hello” 5 times using while loop 
#Exercise 10: Ask password from the user until they enter right password(use while loop) 
#Exercise 11: Keep looping until user types “stop”(while loop)

User_Name=input("Enter your name:")
print("Greetings", User_Name)

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
add=num1+num2
sub=num1-num2
prod=num1*num2
div=num1/num2
print("Addition =",add)
print("Subtraction =",sub)
print("Product =",prod)
print("Division =",div)


name=input("Enter you name: ")
for i in range(3):
    print(name)


tests=["Verify login","Verify signup","Verify logout","Verify homepage redirection","Verify tab switch"]
for test in tests:
    print("Testing for testname", test)


number=int(input("Enter number"))
if number%2==0:
    print(number,"is even number")
else:
    print(number,"is odd number")


test_dict={
    "TC_01":"Verify manual signup",
    "TC_02":"Verify signup with google",
    "Tc_03":"Verify login with valid credentials",
    "Tc_04":"Verify login fails with invalid credentials",
    "Tc_05":"Verify logout successfully"
}
for key,value in test_dict.items():
    print(key,":",value)


age=int(input("Enter age "))
if age>=18:
    print("You are eligible to vote")
else:
    print("You cannot vote")


User_age=int(input("Enter you age "))
if (User_age<10):
    print("50% discount")
else:
    print("No discount")


num=0
while num<5:
    print("Hello")
    num+=1


password=""
correct_password="root"
while password!=correct_password:
    password=input("Enter password ")
    if password==correct_password:
        print("Password matched")
    else:
        print("Password doesn't match, try again")


user_input=""
while user_input!="stop":
    print("Looping")
    user_input=input("Enter stop to exit: ")
print("Loop stopped")