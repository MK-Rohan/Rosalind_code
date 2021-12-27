infor = dict()
name_list = list()

def database(name, language, math, english):
    global infor
    tmp = [int(language), int(math), int(english)]
    infor[name] = tmp
    
def sum_aves(nm):
    sums = sum(infor[nm])
    aves = sum(infor[nm])/len(infor[nm])
    infor[nm].append(sums)
    infor[nm].append(aves)
    
def first():
    sco = list()
    for i,st in enumerate(name_list):
        sco.append(infor[st][3])
    numx = sco.index(max(sco))
    numn = sco.index(min(sco))
    print("highest Score student : {}, Score : {}".format(name_list[numx], max(sco)))
    print("lowest Score student : {}, Score : {}".format(name_list[numn], min(sco)))

def total_ave():
    tot_ave = list()
    for nm in name_list:
        tot_ave.append(int(infor[nm][4]))
    total_average = sum(tot_ave) / len(tot_ave)
    print("Every students average score : {}".format(total_average))
    print("Every students number : {}".format(len(name_list)))    

while True:
    data = input("Give your students information : ").split()
    if data[0] == "q":
        break
    else:
        database(data[0], data[1], data[2], data[3])
        name_list.append(data[0])

for nmt in name_list:
    sum_aves(nmt)

first()
total_ave()



# def sum_ave(nm):
#     sums = sum(infor[nm])
#     aves = sum(infor[nm])/len(infor[nm])
#     nms = nm + "_s"
#     nma = nm + "_a"
#     infor[nms] = sums
#     infor[nma] = aves
