# task_manager_test.py

import heapq

class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        self.task_map = {}
        self.heap = []

        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.task_map:
            userId, _ = self.task_map[taskId]
            self.task_map[taskId] = (userId, newPriority)
            heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.heap:
            neg_priority, neg_taskId, taskId = heapq.heappop(self.heap)
            if taskId in self.task_map:
                userId, current_priority = self.task_map[taskId]
                if -neg_priority == current_priority:
                    del self.task_map[taskId]
                    return userId
        return -1


# Example test case
if __name__ == "__main__":
    tm = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
    tm.add(4, 104, 5)
    tm.edit(102, 8)
    print(tm.execTop())  # Should print 2
    tm.rmv(101)
    tm.add(5, 105, 15)
    print(tm.execTop())  # Should print 5
