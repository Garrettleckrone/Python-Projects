# Second Example From Homework 1
# Garrett Leckrone
# Fall 2017

# Prompt the User for a Positive Integer
posInt = input('Input a Positive Integer\n')

try:
    # Convert the Str to Int
    posInt = int(posInt)
    # If Conversion Succeeds
    print('Success!')
except:
    # If Conversion Does Not Succeed
    posInt = input('No Really...Enter a Positive Integer\n')

    try:
        # Try Again with The New Input
        posInt = int(posInt)
        if type(posInt) == int:
            print("Thanks, you FINALLY entered the right number...")
    except:
        # Tired of your crap, I'm out!
        print('Im done with your crap!')


