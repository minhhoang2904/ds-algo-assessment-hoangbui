class Solution:
    def planVacation(self, miles, target):
        # Time complexity: O(n)
        # Space complexity: O(1)
        
        # Remove pass and write code here
        left = 0
        min_days = len(miles)
        sum = 0
        for i in range(len(miles)):
            sum += miles[i]

            while(sum >= target):
                sum -= miles[left]
                min_days = min(min_days, i - left +1)
                left += 1

        return min_days 



        