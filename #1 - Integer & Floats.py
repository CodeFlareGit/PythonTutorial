#--------Integers--------#
pizza_slices = 1000000
print("We have sold", pizza_slices, "pizza slices this year!")

#--------Floating Point--------#
cost_per_slice = 1.25     #Cost per pizza slice
sales_tax = .093125       #Sales tax - 9.3125%

#--------Formulas--------#
pizza_gross = pizza_slices * cost_per_slice #calcualte pizza cost
sales_tax_cost = sales_tax*(pizza_slices*cost_per_slice) #calcuate sales tax
pizza_net = pizza_gross - sales_tax_cost #calcuate our net cost

print("This results in a net gain of: $", pizza_net)