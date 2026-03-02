clothlist = ["Shirt", "Pant", "Top"]

itr = iter(clothlist)
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))

itr = reversed(clothlist)
print("Reversed iterators")
print(next(itr))

class RemoteControll():
    def __init__(self):
        self.channels = ["sports", "regional", "news"]
        self.index = -1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.index +=1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

r = RemoteControll()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
    

