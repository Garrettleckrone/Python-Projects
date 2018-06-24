numlist = list()
while (True):
    inp = input('Enter a number:  ')
    if inp == 'done': break
    try:
        value = float(inp)
    except:
        print('Enter a real number!')
        continue
    numlist.append(value)
print('The max value in the list is: ' + str(max(numlist)))
print('The min value in the list is: ' + str(min(numlist)))
