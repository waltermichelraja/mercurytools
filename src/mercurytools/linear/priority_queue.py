class PriorityQueue:
    def __init__(self):
        self._data=[]
        self._uses_priority=None
        self._counter=0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"{self.__class__.__name__}({[item[2] for item in self._data]})"

    def push(self,value,priority=None):
        if self._uses_priority is None:
            self._uses_priority=priority is not None
        elif (priority is not None)!=self._uses_priority:
            raise ValueError("cannot mix priority and non-priority values")
        if priority is None:
            entry=(value,self._counter,value)
        else:
            entry=(priority,self._counter,value)
        self._counter+=1
        self._data.append(entry)
        self._heapify_up(len(self._data)-1)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty priority queue")
        self._swap(0,len(self._data)-1)
        _,_,value=self._data.pop()
        self._heapify_down(0)
        return value

    def peek(self):
        if not self._data:
            return None
        return self._data[0][2]

    def to_list(self):
        return [item[2] for item in self._data]


    def _priority(self,item):
        return item[0]

    def _parent(self,i):
        return (i-1)//2

    def _left(self,i):
        return 2*i+1

    def _right(self,i):
        return 2*i+2

    def _swap(self,i,j):
        self._data[i],self._data[j]=self._data[j],self._data[i]

    def _heapify_up(self,i):
        while i>0:
            p=self._parent(i)
            try:
                if (self._data[i][0],self._data[i][1])<(self._data[p][0],self._data[p][1]):
                    self._swap(i,p)
                    i=p
                else:
                    break
            except TypeError:
                raise TypeError("values are not comparable for priority queue")

    def _heapify_down(self,i):
        size=len(self._data)
        while True:
            left=self._left(i)
            right=self._right(i)
            smallest=i
            try:
                if left<size and (self._data[left][0],self._data[left][1])<(self._data[smallest][0],self._data[smallest][1]):
                    smallest=left
                if right<size and (self._data[right][0],self._data[right][1])<(self._data[smallest][0],self._data[smallest][1]):
                    smallest=right
            except TypeError:
                raise TypeError("values are not comparable for priority queue")
            if smallest!=i:
                self._swap(i,smallest)
                i=smallest
            else:
                break