l = [12, 13, 14, "Amber", "Jobie43"]

print(l[0])
print(l[1])
print(l[4])
print(l[-1])

print(type(l))

print(l[0:3])
print(l[0:3][2])
print(l[:][2])
print(l[::][2])
print(l[::][-1])
print(l[4:0:-1])
print(l[4:1:-1])




# Loops
n = ["USA", "CANADA", "UK", "AUSTRALIA", "INDIA", "NEWZEALAND", "GERMANY", "FRANCE", "SOUTH AFRICA"]
additional_countries = ["MEXICO", "PORTUGAL"]
#Create an empty list named k
k = []
# Add the values at index 1 and 4 to k
for i in [1,4]:
    k.append(n[i])
# Using a nested loop to call the additional items
for i in additional_countries:
    k.append(i)

print(k)

h = []
extra_countries = ["DUBAI", "KUWAIT"]
# Add the countries by choosing the index 0,1,2,3
for i in [0,1,2,3]:
    h.append(n[i])
# Using a nested loop to call the additional items
for i in extra_countries:
    h.append(i)

print(h)