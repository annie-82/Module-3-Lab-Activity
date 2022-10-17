#Will show the balance of an account after three years with 5% interest
#Created by Sara Hernandez
#October 16, 2022
#The purpose of this program is to greet the user using their name

#Below shows the beginning balance of the account.
begin = 1000

#Below shows the interest rate of the account.
interest = 0.05

#Below three lines will calculate the years with the interest.
year1 = float(begin)*(1+float(interest))
year2 = float(year1)*(1+float(interest))
year3 = round(float(year2)*(1+float(interest)),2)

#Below three lines will print the sum of each year plus the interest rate.
print('The balance after first year is: $' + str(year1) + '.')
print('The balance after second year is: $' + str(year2) + '.')
print('The balance after third year is: $' + str(year3) + '.')

