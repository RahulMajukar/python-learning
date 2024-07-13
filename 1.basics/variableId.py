a = 50  
b = a  
print(id(a))  #140730236141528
print(id(b))  #140730236141528
# Reassigned variable a  
a = 500  
print(id(a))  #1979586748592