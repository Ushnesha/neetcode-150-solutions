class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sorted_data = sorted(zip(position, speed))

        stk = []
        for pos, speed in sorted_data:
            tgt_t = (target - pos) / speed
            while len(stk) > 0 and tgt_t >= stk[-1][2]:
                stk.pop()
            stk.append([pos, speed, tgt_t])
        return len(stk)
