import json
import heapq as hq
import random

class Courier:
    def __init__(self):
        self.qcourier = []
    def generateCourier(self,count):
        courier = random.randint(3,15)
        hq.heappush(self.qcourier,courier+count)

class OrderDetails:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Order:
    def __init__(self):
        self.q = []
        self.courier = Courier()

    def readJson(self):
        f = open('C:\\Users\mitesh\Desktop\orderDispatch\dispatch_orders.json',)
        self.orderdata = json.load(f)


    def fifo(self):
        count = 0
        idx = 0
        n = len(self.orderdata)
        while True:
            if len(self.q) == 0 and idx >= n:
                return count
            for i in range(1,3):
                if idx < n:
                    orderPrep = int(self.orderdata[idx]['prepTime'])+count
                    hq.heappush(self.q,(orderPrep,idx))
                    self.courier.generateCourier(count)
                idx += 1
            print("At second ", count)

            maxHeapsTop = max(self.q[0][0], self.courier.qcourier[0])

            while len(self.q) > 0 and count >= maxHeapsTop:
                maxHeapsTop = max(self.q[0][0], self.courier.qcourier[0])
                food = hq.heappop(self.q)
                pickup = hq.heappop(self.courier.qcourier)
                print("At time ", pickup,"secs", "Picking up food", self.orderdata[food[1]])

            count += 1
            idx += 2

    def matched(self):
        count = 0
        idx = 0
        matchedq = []
        n = len(self.orderdata)
        while True:
           if len(self.q) == 0 and idx >= n:
               return count

           for i in range(1,3):
               if idx < n:
                   orderPrep = int(self.orderdata[idx]['prepTime'])+count
                   courierTime = random.randint(3,15)+count
                   hq.heappush(matchedq,(max(orderPrep,courierTime),idx))
               idx += 1
           print("At second", count)
           while len(matchedq) > 0 and count >= matchedq[0][0]:
               food = hq.heappop(matchedq)
               print("At time ", count, "secs", "Picking up food", self.orderdata[food[1]])

           count += 1
