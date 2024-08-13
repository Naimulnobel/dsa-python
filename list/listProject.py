x=input('how many days temperature you want to enter?')
list=[]
for i in range(int(x)):
    y=input(f'enter the highest temperature of day {i+1} ')
    list.append(int(y))
print(f'average temperature is {sum(list)/len(list)}')
#average of temperature
avg=sum(list)/len(list)
day=0
for i in range(len(list)):
    if list[i]>avg:
        day+=1

print(f'no of days above average temperature is {day}')



