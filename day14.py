class Difference:
    def __init__(self, a):
        self.__elements = a
        
        self.maximunDifference = 0

	# Add your code here
    # def computeDifference(self):
        # min_item = 101
        # max_item = 0
        # for item in self.__elements:
        #     if item < min_item:
        #         min_item = item
        #     if item > max_item:
        #         max_item = item
        
        # self.maximumDifference = max_item - min_item
        
    def computeDifference(self):
        min_item = min(self.__elements)
        max_item = max(self.__elements)
        self.maximumDifference = max_item - min_item

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)