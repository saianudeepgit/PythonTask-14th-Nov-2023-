print("1. To Covert temperature from Celsius to Fahrenheit")
print("2. To Convert temperature from Fahrenheit to Celsius")
opt = int(input("Choose any option:"))
if opt == 1:
    cel = float(input("Enter temperature in Celsius:"))
    fahr = (cel*9/5)+32
    print("Temperature in Fahrenheit=", fahr)
elif opt == 2:
    fahr = float(input("Enter temperature in Fahrenhite:"))
    cel = (fahr-32)*5/9
    print("Temperature in Celsius=", cel)
else:
    print("Invalid option!!!")
