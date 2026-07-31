li = [1,'A',True, 9999,"Mohan"]

print(li[0])
print(li[1])
print(li[2])
print(li[3])
print(li[4])
# print(li[5])
print("\n")

# While : 

i = 0
n = len(li)
while i<n : 
    print(f"While Loop : {li[i]}")
    i = i+1

print("\n")

# For Loop : 
for item in li:
    print(f"For Loop : {item}")

