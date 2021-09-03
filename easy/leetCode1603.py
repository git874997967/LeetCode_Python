class ParkingSystem(object):
    
    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.bigSize = big  #1
        self.mediumSize = medium  # 2
        self.smallSize = small #3

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            if self.bigSize >= 1:
                self.bigSize -= 1
                return True 
            else:
                return False 
        elif carType == 2:
            if self.mediumSize >= 1:
                self.mediumSize -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.smallSize >=1:
                self.smallSize -= 1
                return True 
            else:
                return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)