# You have a messy user-submitted name: ' jOHN mICHAEL dOE '. Write a function
# clean_name(raw) that strips extra spaces from the edges, collapses any multiple internal
# spaces into one, and capitalises each word properly. Output should be 'John Michael Doe'.

# def clean_name(raw):
#     stripped = raw.strip()          # remove leading/trailing spaces
#     words = stripped.split()        # split removes extra spaces automatically
#     joined = " ".join(words)        # join with single space
#     result = joined.title()         # capitalize each word
#     return result

# print(clean_name(" jOHN mICHAEL dOE "))


#Pythonic version
# def clean_name(raw):
#     return " ".join(raw.split()).title()

# print(clean_name(" jOHN mICHAEL dOE "))