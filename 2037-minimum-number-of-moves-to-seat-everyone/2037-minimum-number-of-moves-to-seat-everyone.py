class Solution(object):
    def minMovesToSeat(self, seats, students):
        list1 =sorted(seats)
        list2 = sorted(students)
        total=0
        for i in range(len(students)):
            total = total + abs(list1[i]-list2[i])
        return total
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        