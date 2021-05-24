import collections

class PoolQueue():
    def __init__(self, max_queue_size):
        self.queue = collections.deque(maxlen=max_queue_size)

    def __len__(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)
        
    def get_queue(self):
        return self.queue

    def get_latest_value(self):
        return self.queue[-1]

    

    
