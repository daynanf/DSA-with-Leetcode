from collections import deque

class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        self.good = 0   

    def consec(self, num: int) -> bool:

        self.queue.append(num)
        if num == self.value:
            self.good += 1

        if len(self.queue) > self.k:
            removed = self.queue.popleft()
            if removed == self.value:
                self.good -= 1

        return len(self.queue) == self.k and self.good == self.k