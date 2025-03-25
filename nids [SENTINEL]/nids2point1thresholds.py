import time
from collections import defaultdict

class Threshold:
    def __init__(self, count, window, group_key, unique_key):
        self.count = count  
        self.window = window  
        self.group_key = group_key  
        self.unique_key = unique_key  
        self.windows = defaultdict(list)  

    def is_exceeded(self, packet):
        group = self.group_key(packet)
        unique = self.unique_key(packet)
        current_time = time.time()
        self.windows[group] = [p for p in self.windows[group] if p["time"] > current_time - self.window]
        if any(p["key"] == unique for p in self.windows[group]):
            return False  
        self.windows[group].append({"time": current_time, "key": unique})
        return len(self.windows[group]) > self.count