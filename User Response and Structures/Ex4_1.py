def ex51():
    total = 0
    count = 0
    while (True):

        inp = input('Enter a number\n')
        # If user enters 'done'
        if inp == 'done': break

        # I couldn't get around a way of temporarily storing numbers. I'm not storing ALL the inputted values,
        # like a list but I don't know how I could get around having variables for total, count and average.

        try:
            value = float(inp)
        except:
            print('I said a number!')
            continue
        total = total + value
        count = count + 1
        average = total / count

    print(
        'The count is: ' + str(count) + '. The total is: ' + str(total) + '. And the average is: ' + str(average) + '.')
def ex52():
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

while(True):
    inp = input('Would you like to computer Ex51 or Ex52? Or enter "done"\n')
    if inp == 'done': break
    try:
        if inp == 'Ex52':
            ex52()
            break
        if inp == 'Ex51':
            ex51()
            break
    except:
        print('Enter "Ex51" or "Ex52"')
        continue


