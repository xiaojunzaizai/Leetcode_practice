class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.dic = {'big':self.big,'medium': self.medium,'small':self.small}

    def addCar(self, carType: int) -> bool:
        d_type = {1:'big',2:'medium',3:'small'}
        n = self.dic[d_type[carType]]
        if n-1 >=0:
            self.dic[d_type[carType]] = n -1
            return True
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
'''
Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]

Output
[null, true, true, false, false]
'''