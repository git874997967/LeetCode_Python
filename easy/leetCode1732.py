#1732. Find the Highest Altitude
def largestAltitude(gain):
    altitude = [0]
    for i in range(1,len(gain)+1):
        altitude.append(gain[i-1] + altitude[i-1])
    print(max(altitude),altitude)


largestAltitude([-5,1,5,0,-7])