#take user input
#Convert input to str
userInput = str (input(" Give me a character to turn into a diamond..."))
#diamond variable 1 
d_1 = userInput+" "

#diamond variable 2
d_2 = userInput+" "+userInput+" "+userInput+" "+userInput

#diamond variable 3
d_3 = userInput+" "+userInput+" "+userInput+" "+userInput

#diamond variable 4
d_4 = userInput+" "+userInput+" "+userInput+" "+userInput

#print , 1.2.3.4.1.2.3.4
print(d_1)
print(d_2)
print(d_3)
print(d_4)