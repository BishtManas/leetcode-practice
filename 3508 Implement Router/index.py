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


# ----------------------
# Example usage (testing)
# ----------------------
if __name__ == "__main__":
    router = Router(3)

    print(router.addPacket(1, 2, 10))  # True
    print(router.addPacket(2, 3, 15))  # True
    print(router.addPacket(4, 2, 12))  # True
    print(router.addPacket(5, 6, 20))  # This will remove the oldest packet

    print(router.forwardPacket())      # Removes & returns the oldest in queue
    print(router.getCount(2, 5, 15))   # Count packets going to destination 2 within [5,15]
    print(router.getCount(3, 10, 20))  # Count packets going to destination 3 within [10,20]
