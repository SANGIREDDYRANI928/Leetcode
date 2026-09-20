import heapq

class MedianFinder(object):

    def __init__(self):
        self.left = []    # max heap
        self.right = []   # min heap

    def addNum(self, num):

        # Add to left max heap
        heapq.heappush(self.left, -num)

        # Make sure every left element <= every right element
        if self.left and self.right and -self.left[0] > self.right[0]:
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)

        # Balance sizes
        if len(self.left) > len(self.right) + 1:
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)

        elif len(self.right) > len(self.left):
            x = heapq.heappop(self.right)
            heapq.heappush(self.left, -x)

    def findMedian(self):

        if len(self.left) > len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2.0