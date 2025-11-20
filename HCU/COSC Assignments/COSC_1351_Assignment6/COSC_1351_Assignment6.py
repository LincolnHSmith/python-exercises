
errorsFile = open('errors.txt', 'r')
errors = errorsFile.read()


#Function to sanitize inputs
def sanitize(text):
    for ch in text:
        if ch in errors:
            return sanitize(input("Try again!\n"))
        
    return True

print(sanitize("Hello!"))