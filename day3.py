
names={"India":10,"USA":90,"UK":78}
max=0
str=""
for i in names:
    for j in i:
        if names [i] > max:
            str=i
            max= names[i]
print(str)
