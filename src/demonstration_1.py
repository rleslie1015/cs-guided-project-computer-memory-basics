"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
        76
Output: "lambdaschool"
        108
Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    lower_st = ''
    # Your code here
    for i in string:
     
        int_val = ord(i) # return int
        if int_val >= 65 and int_val <= 90:
            lower_int_val = int_val + 32
            lower_st += chr(lower_int_val)
        else: 
            lower_st += i
   
    return lower_st

    
print(to_lower_case("LambdaSchool"))
print(to_lower_case("LLAMA"))