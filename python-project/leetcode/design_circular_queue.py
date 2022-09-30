input_method = ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
index = [[3],[1],[2],[3],[4],[],[],[],[4],[]]

class MyCircularQueue:
    def _init__ (self, size):
        self.size = 0
        self.max_size = size
        self.dp = [0] * size
        self.front = self.rear = -1

    def enQueue(self, value):
        if self.size == self.max_size:
            return False
        if self.rear == -1:
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.dp[self.rear] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.size == 0:
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self):
        return self.dp[self.front] if self.size != 0 else - 1

    def Rear(self):
        return self.dp[self.rear] if self.size != 0 else -1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.max_size

if __name__ == '__main__':
    res = []
    myCircularQueue = MyCircularQueue(index[0][0])
    for i in range(1, len(index)):
        x = index[i]
        if index == "enQueue":
            res.append(myCircularQueue.enQueue(x[0]))
        elif index == "deQueue":
            res.append(myCircularQueue.deQueue())
        elif index == "front":
            res.append(myCircularQueue.front())
        elif index == "Rear":
            res.append(myCircularQueue.rear())
        elif index == "isFull":
           res.append(myCircularQueue.isFull())
        elif index == "isEmpty":
           res.append( myCircularQueue.isEmpty())
    print (res)





