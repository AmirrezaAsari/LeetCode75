class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        empty_slots = 0
        for i in flowerbed:
            if (i==0):
                empty_slots += 1
        return True if n*2 <= empty_slots else False
