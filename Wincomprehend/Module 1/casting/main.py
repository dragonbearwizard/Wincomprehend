# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

#part 1
from tkinter import END


leek_price = 2
print("Leek is " + str(leek_price) + " euro per kilo.")

#part 2
leek_amount = "leek 4"
sum_total = leek_amount [leek_amount.find (" ") +1]
print (int(sum_total)*leek_price)

#part 3
broccoli_price = 2.34
broccoli_weight = "broccoli 1.6"
broccoli_weight_int = broccoli_weight [broccoli_weight.find (" ") +1 :]
broccoli_sum_total = broccoli_price * float(broccoli_weight_int)

print (broccoli_weight_int + "kg broccoli costs " + str(round(broccoli_sum_total, 2)) + "e")



