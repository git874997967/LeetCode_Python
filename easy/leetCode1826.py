#1826. Faulty Sensor
def badSensor(s1, s2):
      # base case 
      # the same end cannot get the result
      if len(s1) < 2 or s1[:-1] == s2[:-1]:
          return - 1
      lens = len(s1)
      for i in range(lens-1):
          if s1[i] != s2[i]:
              if s1[i+1:] == s2[i:-1] and s2[i+1:] == s1[i:-1]:
                  return - 1
              if s1[i+1:] == s2[i:-1]:
                  return 2
              if s1[i:-1] == s2[i+1:]:
                  return 1
      

print(badSensor([2,3,2,2,3,2],[2,3,2,3,2,7]))