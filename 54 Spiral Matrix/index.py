from collections import deque, defaultdict
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.packet_set = set()
        self.dest_map = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packet_set:
            return False

        if len(self.queue) == self.memoryLimit:
            old_s, old_d, old_t = self.queue.popleft()
            self.packet_set.remove((old_s, old_d, old_t))
            idx = bisect.bisect_left(self.dest_map[old_d], old_t)
            if 0 <= idx < len(self.dest_map[old_d]) and self.dest_map[old_d][idx] == old_t:
                self.dest_map[old_d].pop(idx)

        self.queue.append(key)
        self.packet_set.add(key)
        bisect.insort(self.dest_map[destination], timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        s, d, t = self.queue.popleft()
        self.packet_set.remove((s, d, t))
        idx = bisect.bisect_left(self.dest_map[d], t)
        if 0 <= idx < len(self.dest_map[d]) and self.dest_map[d][idx] == t:
            self.dest_map[d].pop(idx)
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dest_map[destination]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        return right - left
