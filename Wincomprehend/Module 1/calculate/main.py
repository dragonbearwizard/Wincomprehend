# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line

#product price
broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

#number of products
num_broccolis = 5
num_leeks = 2
num_potatoes = 7
num_brussel_sprouts = 10

#solutions
sum_one_each = broccoli + leek + potato + brussel_sprout
avg_price = sum_one_each / 4
sum_total = potato * num_potatoes + leek * num_leeks + broccoli * num_broccolis + brussel_sprout * num_brussel_sprouts
discount_percentage = 30
discounted_price = sum_total * discount_percentage / 100 
discounted_sum_total = sum_total - discounted_price

print (discounted_sum_total)
"10"
"4"
"21"
"70"
"hint: note the variable name already says 'percent'"


