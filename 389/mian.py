
noskill = []
firstskill = []
secondskill = []

for i in range(90):
    noskill.append(0)
    firstskill.append(0)
    secondskill.append(0)

days = int(input())
for count in range(1,days+1):
#    print(count)
    if count == 1:
        noskill[count] = 1
        firstskill[count] = 1
        secondskill[count] = 0

    else:
        noskill[count] = noskill[count-1] + secondskill[count-1]
        firstskill[count] = noskill[count-1]
        secondskill[count] = firstskill[count-1]
#    print(noskill[count]+firstskill[count]+secondskill[count])

#print(noskill[days])
result = noskill[days] + secondskill[days]
print(result)
