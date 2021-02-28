Hops=20;
trial = 1000
dr=0.01
fileSize=10000
subSize= 500
p_delay=1
from random import random
res = {"message":{},"packet":{}}
def ave(d):
    return sum(d.values())/len(d.values())

def run():
    for trial_num in range(trial):
        time_taken = 0
        state = 0
        t_delay=fileSize
        while state<Hops:
            if random()>dr:
                state+=1
            time_taken+=3*p_delay+t_delay
        res["message"][trial_num]=time_taken


    for trial_num in range(trial):
        time_taken = 0
        state = 0
        t_delay=subSize
        while state<Hops:
            currentSent = 0
            while currentSent<fileSize:
                if random()>dr:
                    currentSent+=subSize
                time_taken+=3*p_delay+t_delay
            state+=1
        res["packet"][trial_num]=time_taken
    print(f"With message switching on average it takes:{ave(res['message'])} with packet switching on average it takes:{ave(res['packet'])} epochs")
    print(f"Ratio of averages are message/packet={ave(res['message'])/ave(res['packet'])}")


if __name__=="__main__":
    run()
