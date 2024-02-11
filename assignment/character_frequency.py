sample_string = 'semicolon.africa'
count = {}
for i in sample_string:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1
print(count)