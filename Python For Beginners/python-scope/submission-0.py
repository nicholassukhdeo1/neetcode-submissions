def add_one(n):
    n = n + 1
    print(n)   

n = 10

add_one(n)     # Output: 11

print(n)       # Output: ?

# print will print 10 because the update on n is forgotten
# after the fxn call ends
