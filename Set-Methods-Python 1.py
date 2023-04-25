


#----------------------
#--- Set Methods---
#-----------------------



# Clear()

a = {1,2,3}
a.clear()
print(a) # set()


# Union()


b = {"One" , "Two" , "Three"}
c = {"1" "2" , "3"}
x = {"Salar" , "Issa"}

print(b.union(c)) # {'3', 'Three', '12', 'One', 'Two'}
print(b.union(c,x)) # {'12', 'Salar', 'One', 'Issa', 'Two', '3', 'Three'}


# Add()

e = {1,2,3,4}
e.add(5) # {1, 2, 3, 4, 5}
e.add(6) # {1, 2, 3, 4, 5, 6}
print(e) 


# copy()

d = {1,2,3,4,5}
f = d.copy()

print(d) # {1, 2, 3, 4, 5}
print(f) # {1, 2, 3, 4, 5}

d.add(6)

print(d) # {1, 2, 3, 4, 5, 6}
print(f) # {1, 2, 3, 4, 5}



# remove()

g = {1,2,3,4,5,6}
g.remove(1) # {2, 3, 4, 5, 6}
g.discard(7) # Error
print(g) 


# Discard()

y= {1,2,3,4,5,6}
y.discard(1) # {2, 3, 4, 5, 6}
y.discard(7) # without Error {1, 2, 3, 4, 5, 6}
print(y)


# pop()

a = {"salar" , True, "Issa" , 20 , 50.42}
print(a.pop()) # Random Elements  # Issa # True # salar # 



# Update()

u = {1,2,3}
h = {"A" , "salar" , "B" , 1}
u.update(["html" , "Css"])# {1, 2, 3, 'Css', 'salar', 'A', 'B', 'html'}
u.update(h)
print(u) # {1, 2, 3, 'A', 'salar', 'B'}






