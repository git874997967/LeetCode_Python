# 606. Construct String from Binary Tree
def tree2str(root):
    result = []
    def toStr(root):
        if root:
            result.append("(")
            result.append(str(root.val))
            if root.left and root.right:
                toStr(root.left)
                toStr(root.right) 
            elif root.right:
                result.append("()")
                toStr(root.right)
            elif root.left:
                toStr(root.left())
            result.append(")")
    toStr(root)
    return "".join(result[1:len(result)-1])


def tree2str(self,root):
    if not root:
        return ""
    result = str(root.val)
    if root.left:
        result += "(" + self.tree2str(root.left) + ")"
        if root.right:
            result += "(" + self.tree2str(root.right) + ")"
    elif root.right:
        result += "()(" + self.tree2str(root.right) + ")"
    return result
     


