import Agent
import matplotlib as plt

def Singlewalk(duration):
    cashew = agent.Agent()
    time = 0
    xhis = []
    yhis=[]
    this = []
    dhis = []

    while time < duration:
        cashew.step()
        xhis.append(cashew.x)
        yhis.append(cashew.x)
        this.append(time)
        dhis.append(cashew.x)


