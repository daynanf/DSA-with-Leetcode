class RecentCounter:

    def __init__(self):
        self.count=[]

    def ping(self, t: int) -> int:
        if not self.count:
            self.count.append(t) 
        elif abs(self.count[0]-t)<=3000:
            self.count.append(t)
        else:
            while self.count and abs(self.count[0]-t)>3000:
                self.count.pop(0)
            self.count.append(t)
        return len(self.count)  


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)