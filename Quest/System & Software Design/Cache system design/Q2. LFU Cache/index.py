from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        # key -> (value, frequency)
        self.key_map = {}

        # frequency -> OrderedDict of keys (to maintain LRU order)
        self.freq_map = defaultdict(OrderedDict)

        # minimum frequency in the cache
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1

        value, freq = self.key_map[key]

        # Remove key from current frequency list
        del self.freq_map[freq][key]

        # If this was the last key of min_freq, update min_freq
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Add key to next frequency list
        self.freq_map[freq + 1][key] = None
        self.key_map[key] = (value, freq + 1)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_map:
            # Update value and frequency
            self.key_map[key] = (value, self.key_map[key][1])
            self.get(key)
            return

        # If cache is full, remove LFU key
        if self.size == self.capacity:
            lfu_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.key_map[lfu_key]
            self.size -= 1

            if not self.freq_map[self.min_freq]:
                del self.freq_map[self.min_freq]

        # Insert new key with frequency = 1
        self.key_map[key] = (value, 1)
        self.freq_map[1][key] = None
        self.min_freq = 1
        self.size += 1
