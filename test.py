# def hashf(a):
#     for s in a:
#         print(s, ord(s))

# hashf("anthony")

# def hashf(a):
#     for s in a:
#         total = 0
#         total += ord(s)

#     return total

table = [None] * 8
##  PUT
def hashf(s):
     total = 0

     bytes = str(s).encode()

     for b in bytes:
         total += b
        
     return total

def get_index(s):
    value = hashf(s)

    return value % len(table)

def put(key, value):
    index = get_index(key)
    table[index] = value

def get(key):
    index = get_index(key)
    value = table[index]

    return value

put("Anthony", 1616)
put("peep", 9009)

'''
index = get_index("Anthony")
table[index] = 1616

index = get_index("peep")
table[index] = 9009
'''

print(table)

print(get("Anthony"))
print(get("peep"))

"""
0(n) over then length (number of bytes) of the key
0(1) over the number of items in the table

"""