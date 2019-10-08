import random

class PuzzlePlane:
     empty_element = 0

    # initializes plane with shufffeled numbers from range <1,15>
    def __init__(self):
        self.plane = []
        
        # todo: remove magic numbers
        numbers = []
        for n in range(0,16):
            numbers.append(n)

        random.shuffle(numbers)
    
        #todo: move to distinct function
        start = 0
        begin = 4

        #getting indices of the empty element
        self.empty_element_index = numbers.index(self.empty_element)
        self.empty_element_index = [int(self.empty_element_index/4), int(self.empty_element_index % 4) ]
    

        while begin <= 16:
            self.plane.append(numbers[start:begin])
            start += 4
            begin += 4
        

    # returns index of an empty elemenet
    def empty_element_index(self):
        return self.empty_element_index


    def move_down(self):


    def move_up(self):

    def move_right(self):

    def move_left(self):