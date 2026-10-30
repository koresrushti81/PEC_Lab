class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BST:
    def insertNode(self,r,data):
        if r is None:
            r=Node(data)
        else:
            r1=r
            while r1 is not None:   
                if data < r1.data:
                    if r1.left is None:
                        r1.left=Node(data)
                        break
                    r1=r1.left
                elif data > r1.data:
                    if r1.right is None:
                        r1.right=Node(data)
                        break
                    r1=r1.right
        return r

    def LOT(self,r):
        if r is None:
            return 
        que=[]
        que.append(r)
        while que:
            curr=que.pop(0)
            print(curr.data,end=" ") 
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
                
    def PreorderI(self,r):
        if r is None:
            return
        st=[]
        st.append(r)
        while st:
            curr=st.pop()
            print(curr.data,end=" ")
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
                
    def InorderI(self,r):
        if r is None:
            return
        st=[]
        curr=r
        while True:
            if curr:
                st.append(curr)
                curr=curr.left
            elif st:
                curr=st.pop()
                print(curr.data,end=" ")
                curr=curr.right
            else:
                break
            
    def PostorderI(self,r):
        if r is None:
            return
        s1=[]
        s2=[]
        s1.append(r)
        while s1:
            curr=s1.pop()
            s2.append(curr)
            
            if curr.left:
                s1.append(curr.left)
            if curr.right:
                s1.append(curr.right)
                
        while s2:
            c=s2.pop()
            print(c.data,end=" ")


    
root=None
b=BST()
root=b.insertNode(root,45)
root=b.insertNode(root,23)
root=b.insertNode(root,78)
root=b.insertNode(root,90)
root=b.insertNode(root,12)
root=b.insertNode(root,43)
root=b.insertNode(root,56)
root=b.insertNode(root,100)
root=b.insertNode(root,34)
print("level")
b.LOT(root)
print()
print()
print("preorder")
b.PreorderI(root)
print()
print()
print("inorder")
b.InorderI(root)
print()
print()
print("postorder")
b.PostorderI(root)