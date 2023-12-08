class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if root == None: return ""

        now = str(root.val)
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if left=="" and right=="": return now
        if right=="": return now + "(" +left+ ")"
        return now + "(" +left+ ")(" +right+ ")"