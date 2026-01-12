#1.Ask the user for total test cases and passed test cases, then print failed test cases
Total_TestCases= int (input("Enter total test cases: "))
Passed_TestCases= int (input("Enter total passed test cases: "))
print("Failed test cases are:",Total_TestCases-Passed_TestCases)

# 2.Create variables for expected status code and actual status code, then print if they are the same.
Expected_code= 404
Actual_Code= 403
print(Expected_code==Actual_Code)

# 3.Create a variable retry_count = 1, add 2 to it, then print the final retry count.
retry_count=1
retry_count +=2
print(retry_count)

# 4.Create Boolean variables:login_success = True dashboard_visible = True error_message = False print: login_success and dashboard_visible,login_success and not error_message,error_message or dashboard_visible
Login_Success = True
Dashboard_Visible = True
Error_Message = False
print("Result of Login success and Dashboard Visible: ", Login_Success and Dashboard_Visible)
print("Result of Login success and not Error message: ", Login_Success and not Error_Message)
print("Result of Error message or Dashboard visible: ", Error_Message or Dashboard_Visible)

# 5.Create a list of 3 test case names, a tuple of 2 browser names, and a dictionary with username and password. Print all of them.
TestCases_List=["Login_TC_001","SignUp_TC_001","Logout_TC_001"]
Browser_tup=("Chrome","Brave")
User_Passw_Disct={
    "User": "Shruti",
    "Password": "Shruti@123"
}
print("Test cases name: ", TestCases_List)
print("Browser name: ", Browser_tup)
print("User name: ", User_Passw_Disct.keys() )
print("User password", User_Passw_Disct.values())