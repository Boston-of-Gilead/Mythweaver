import numpy as np

remHunts = 3

list = ['Mythweaver','Grammarian']
arM = 0.3985
arG = 0.6015
hunt = []

def runH():
    global remHunts
    result = np.random.choice(list,1, p=[arM, arG])
    # print(result)
    if result == 'Mythweaver':
        hunt.append("Mythweaver")
        remHunts = remHunts + 2
    else:
        hunt.append("Grammarian")

while remHunts != 0:
    runH()
    remHunts = remHunts - 1

print(hunt)