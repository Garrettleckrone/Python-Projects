def computepay(hour, payrate):
    if hour <= 40:
        return hour * payrate
    if hour > 40:
        return 40 * payrate + (hour - 40) * (1.5 * payrate)

print('Testing computepay')
print('Testing with hours = 45 and payrate = 10. Expected pay: 475.0')
print(computepay(45,10))