from typing import List
import bisect
import time

class Solution:
    """
    Solves the 'Avoid Flood in The City' problem using a greedy approach 
    with a sorted list to manage available dry days.
    """
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        
        # Dictionary: {lake_id: day_index}
        # Stores the day a lake was LAST filled.
        last_rain_day = {}
        
        # Sorted list of indices of the available dry days (rains[i] == 0).
        dry_days = []
        
        for i in range(n):
            lake_id = rains[i]
            
            if lake_id > 0:
                # --- Rain Day ---
                
                if lake_id in last_rain_day:
                    last_fill_day = last_rain_day[lake_id]
                    
                    # Find the EARLIEST dry day (index j) available AFTER last_fill_day
                    # bisect_left finds the insertion point for last_fill_day, 
                    # which is the index of the first element > last_fill_day.
                    insert_point = bisect.bisect_left(dry_days, last_fill_day)
                    
                    if insert_point == len(dry_days):
                        # No dry day available between the two rainfalls
                        return []
                    
                    # Schedule the drying: Use the found dry day (dry_days[insert_point])
                    dry_day_index = dry_days.pop(insert_point) # Pop removes it and shifts elements
                    
                    # Assign the lake to be dried on that day
                    ans[dry_day_index] = lake_id

                # Update the last time this lake was filled
                last_rain_day[lake_id] = i

            else:
                # --- Dry Day (rains[i] == 0) ---
                
                # Add the index of this dry day to the available list, keeping it sorted.
                bisect.insort(dry_days, i)
                
                # Default action for an unscheduled dry day. 
                # Since all lakes start empty, drying any empty lake (e.g., lake 1) 
                # is harmless and required by the problem structure (ans[i] must be > 0).
                ans[i] = 1 
                
        return ans

# Example Usage for VS Code/Local Environment
if __name__ == '__main__':
    solver = Solution()

    # Example 1: [1,2,3,4] -> [-1,-1,-1,-1]
    rains1 = [1, 2, 3, 4]
    result1 = solver.avoidFlood(rains1)
    print(f"Input: {rains1}\nOutput: {result1}") 

    # Example 2: [1,2,0,0,2,1] -> [-1,-1,2,1,-1,-1]
    rains2 = [1, 2, 0, 0, 2, 1]
    result2 = solver.avoidFlood(rains2)
    print(f"\nInput: {rains2}\nOutput: {result2}") 

    # Example 3: [1,2,0,1,2] -> []
    rains3 = [1, 2, 0, 1, 2]
    result3 = solver.avoidFlood(rains3)
    print(f"\nInput: {rains3}\nOutput: {result3}") 

    # Example 4: [69,0,89,89,89,89] -> [] (Flood on day 3)
    rains4 = [69, 0, 89, 89, 89, 89] 
    result4 = solver.avoidFlood(rains4)
    print(f"\nInput: {rains4}\nOutput: {result4}")