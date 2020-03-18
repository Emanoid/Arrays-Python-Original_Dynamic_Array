import array as array
import ctypes as c

class MyList:
    def __init__(self):
        self._capacity = 10
        self._length = 0
        self._elements = (self._capacity * c.py_object)()
        for i in range(self._capacity):
            self._elements[i] = 0
    
    def get_cap(self):
        return self._capacity

    def _len_(self):
        return self._length

    def get_elem(self):
        return self._elements

    def _getitem_(self,index):
        return self._elements[index]

    def append(self, item):
        if self._length <= self._capacity-1:
            self._elements[self._length] = item
            self._length += 1 
        else:
            temp = (self._capacity * c.py_object)()
            len = 0
            for i in range(self._length):
                temp[i] = self._elements[i]
                len += 1
            self._capacity += 10
            self._elements = (self._capacity * c.py_object)()
            for i in range(self._capacity):
                self._elements[i] = 0
            for i in range(len):
                self._elements[i] = temp[i]
            self._elements[self._length] = item
            self._length += 1

    def remove(self, item):
        temp = (self._length * c.py_object)()
        for i in range(self._length):
            temp[i] = self._elements[i]
        bindex = 0
        for i in range(self._length):
            if temp[i] == item:
                bindex = 0 + i
        ntemp1 = ((self._length-1) * c.py_object)()
        ntemp = self.removehelper(ntemp1,temp,bindex,self._length)
        for i in range(self._capacity):
                self._elements[i] = 0
        for i in range(self._length-1):
            self._elements[i] = ntemp[i]
        self._length -= 1   

    def removehelper(self,l1,l2,bi,len):
        i = 0
        b = 0
        while i <= len-2:
            if i != bi:
                l1[i] = l2[b]
                i = i + 1
                b = b + 1
                #print(i)
            elif i == bi:
                b = b + 1
                l1[i] = l2[b]
                print(b)
                i = i + 1
                b = b + 1
        return l1                 
    
    def print_elements(self):
        print(self._elements[0:self._length])

#test
ML = MyList()
for i in range(45):
    ML.append(i+1)
ML.print_elements()
print("Index 12: ",ML._getitem_(12))
print("Capacity: ",ML.get_cap())
print("Length: ",ML._len_())



        
