class PriorityQueue:
    def __init__(self):
        self._data=[]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"PriorityQueue({self._data})"

    def push(self,value):
        self._data.append(value)
        self._heapify_up(len(self._data)-1)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty priority queue")
        self._swap(0,len(self._data)-1)
        value=self._data.pop()
        self._heapify_down(0)
        return value

    def peek(self):
        if not self._data:
            return None
        return self._data[0]

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
            if self._data[i]<self._data[p]:
                self._swap(i,p)
                i=p
            else:
                break

    def _heapify_down(self,i):
        size=len(self._data)
        while True:
            left=self._left(i)
            right=self._right(i)
            smallest=i
            if left<size and self._data[left]<self._data[smallest]:
                smallest=left
            if right<size and self._data[right]<self._data[smallest]:
                smallest=right
            if smallest!=i:
                self._swap(i,smallest)
                i=smallest
            else:
                break