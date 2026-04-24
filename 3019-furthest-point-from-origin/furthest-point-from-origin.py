class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        numR=moves.count("R")
        numL=moves.count("L")
        num_=moves.count("_")
        if numR>numL:
            return numR+num_-numL
        elif numR<numL:
            return numL+num_-numR
        else:
            return num_