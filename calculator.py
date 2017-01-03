print('This program calcluates Fahrenheit to Celsius')

f_string= input('Enter the temperature in Fahrenheit:')

f=float(f_string)

c= (f-32) * 5 / 9

print('The temperature in Celsius is:' + str(c) + 'degrees')

print('This program calculates the area of a triangle.')

b_string= input('enter the base length:')

b=float(b_string)

h_string= input('enter the height of the triangle:')

h=float(h_string)

a = (1/2)* b*h

print('The area of this triangle is: ' + str(a) + " units.")
