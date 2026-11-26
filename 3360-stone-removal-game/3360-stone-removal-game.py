class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        remove = 10
        alice = True

        while n >= remove:
            n -= remove
            remove -= 1
            alice = not alice

        return not alice