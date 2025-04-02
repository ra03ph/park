src = 'a2b3c6a2c3f1g1'
output = ''
i = 0

while i < len(src):
    char = src[i]
    i += 1
    count = 0
    
    while i < len(src) and src[i].isdigit():
        count = count * 10 + int(src[i])
        i += 1
    
    output += char * count

print("output =", output)
