

input = "AAACCBBCCCBCC"


curr = {'char': None, 'count': 0}
for char in input:
    if curr['count'] == 0:
        curr['char'] = char
        curr['count'] = 1
    else:
        if char == curr['char']:
            curr['count'] += 1
        else:
            curr['count'] -= 1

print "%s is the majority element" % curr['char'] 
