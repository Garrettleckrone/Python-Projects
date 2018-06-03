total = 0
count = 0
while (True):

    inp = input('Enter a number\n')
    # If user enters 'done'
    if inp == 'done': break

    # I couldn't get around a way of temporarily storing numbers. I'm not storing ALL the inputted values,like a list
    # but I don't know how I could get around having variables for total, count and average.

    try:
        value = float(inp)
    except:
        print('I said a number!')
        continue
    total = total + value
    count = count + 1
    average = total/count

print('The count is: ' + str(count) + '. The total is: ' + str(total) + '. And the average is: ' + str(average) + '.')