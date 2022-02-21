data = input("Give your numbers: (months) and (rabbit)")
months = data.split()[0]
rabbits = data.split()[1]
children = 1
adults = 0
new_baby = 0

def growth ():
    global adults, children
    adults += children
    children -= children

def baby (adult):
    global new_baby, rabbits
    new_baby += adult * int(rabbits)
                               
for i in range(1, int(months)):
    baby(adults)
    growth()
    children += new_baby
    new_baby -= new_baby
                                                        
print("total rabbit's number are", children + adults)
