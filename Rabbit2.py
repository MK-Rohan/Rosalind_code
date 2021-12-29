data = input("Give your numbers: (months) and (rabbit)")
months = data.split()[0]
live_months = data.split()[1]
life_time = dict()
newbone_rabbits = 0
def growth(mnth):
    global newbone_rabbits
    for k in range(2, int(live_months)+1): # newbone_rabbits birth
#         print("birth")
        ID = "growth_" + str(k)
        newbone_rabbits += life_time[ID]
    for l in range(int(live_months), 0, -1):
        if l == int(live_months): # senior rabbits death
#             print("death")
            ids1 = "growth_" + str(l)
            life_time[ids1] = 0
        else: # growth
#             print("growth")
            ids1 = "growth_" + str(l+1)
            ids2 = "growth_" + str(l)
            print(life_time[ids2])
            life_time[ids1] += life_time[ids2]
    life_time["growth_1"] += newbone_rabbits
    newbone_rabbits = 0
    
for i in range(1, int(live_months)+1):
    ID = "growth_" + str(i)
    life_time[ID] = 0
life_time["growth_1"] += 1    

for j in range(1, int(months)+1):
    growth(j)


total_rabbits = 0
for m in range(1, int(live_months)+1):
    ID = "growth_" + str(m)
    total_rabbits += life_time[ID]
print(life_time)
print("Total rabbits number:", total_rabbits)

print()
for l in range(int(live_months), 1, -1):
    print(l)
