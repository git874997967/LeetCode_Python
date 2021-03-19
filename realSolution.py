def get_free_time(cal1,cal2,duration,time):
    free1,free2 =  [], []
    def get_free(cal,time):
        busy,freeTime = list(cal[0]),[]
        for i in range(1,len(cal)):
            if cal[i][0] > busy[1]:
                freeTime.append([busy[1], cal[i][0]])
                busy = list(cal[i])
            else:
                busy[1] = max( busy[1], cal[i][1])
        freeTime.append([time[0],cal[0][0]])
        freeTime.append([cal[-1][1],time[1]]) 
        freeTime.sort(key = lambda x:x[0])
        return freeTime
    free1 = get_free(cal1,time)
    free2 = get_free(cal2,time)
    print(free1,free2)
calendar1 = [(20,100),(200,230),(250,330),(450,500)]
calendar2 = [(30,100),(100,130),(250,330)]
duration = 10
time = (0,500)
get_free_time(calendar1,calendar2,duration,time)