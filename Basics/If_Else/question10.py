# Write a function validate_username(username) that checks a
# username string and returns the FIRST problem it finds (in this order):
# 1. Less than 4 characters → 'Too short' 2. More than 15 characters →
# 'Too long' 3. Contains a space → 'No spaces allowed' 4. Does not start
# with a letter → 'Must start with a letter' 5. Contains characters other
# than letters, digits, underscores → 'Invalid characters' 6. All checks
# pass → 'Valid' Test: 'hi', 'this_is_a_very_long_name_123', 'user name',
# '123abc', 'user@name', 'good_user1'


def validate_username(username):
    if len(username) < 4:
        return "Too short"
    elif len(username) > 15:
        return "Too long"
    elif ' ' in username:  
        return "No spaces allowed"
    elif not username[0].isalpha():  
        return "Must start with a letter"
    elif not username.isidentifier():  
        return "Invalid characters"
    else:
        return "Valid"


print(validate_username("hi"))                      
print(validate_username("this_is_a_very_long_name_123"))  
print(validate_username("user name"))               
print(validate_username("123abc"))                   
print(validate_username("user@name"))                 
print(validate_username("good_user1"))                

    