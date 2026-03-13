class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL():
    def __init__(self):
        self.head=None

    def insertbeg(self):
        newnode=Node(5)
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode

    def insertend(self):
        newnode=Node(50)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp 


    def insertpos(self):
        pos=4
        newnode=Node(25)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        newnode.prev=temp
        newnode.next=temp.next
        temp.next=newnode
        temp.next.prev=newnode    
 


    def delete_beg(self):
        temp=self.head
        self.head=self.head.next
        self.head.prev=None
        temp.next=None


    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None    

    def delete_pos(self):
        temp=self.head.next
        before=self.head
        pos=3
        for i in range(1,pos-1):
            temp=temp.next
            before=before.next 
        before.next=temp.next  
        temp.next.prev=before
        temp.prev=None
        temp.next=None



    def reverse(self):
        prev=None
        temp=self.head
        while temp:
            newnode=temp.next
            temp.next=prev
            temp.prev=newnode
            prev=temp
            temp=newnode
        self.head=prev  



    def reverse2(self):   #2nd method to reverse
        stack=[]
        temp=self.head
        while temp:
            stack.append(temp.data)
            temp=temp.next
        temp=self.head
        while temp:
            temp.data=stack.pop()
            temp=temp.next



    def palindrome(self):
        stack=[]
        temp=self.head
        while temp:
            stack.append(temp.data)
            temp=temp.next
        temp=self.head
        while temp:
            if stack.pop()!=temp.data:
                return False
            else:
                temp=temp.next
        return True 


    def count(self):
        self.count=0
        temp=self.head
        while temp:
            self.count+=1
            temp=temp.next
        return self.count  

    def middle(self):
        slow=self.head
        fast=self.head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next  
        return slow.data   


    def sortedremove(self):
        temp=self.head
        while temp and temp.next:
            if temp.data!=temp.next.data:
                temp=temp.next
            else:    
                temp.next=temp.next.next  

    def unsortedrem(self):
        s=set()
        prev=None
        temp=self.head
        while temp:
            if temp.data not in s:
                s.add(temp.data)   
                prev=temp
                temp=temp.next
            else:
                prev.next=temp.next
                temp=temp.next
                            




    def display(self):
        if self.head is None:
            print('empty')
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end='-->') 
                temp=temp.next       
l=DLL()
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(10)
n2.next=n3
n3.prev=n2
n4=Node(40)
n3.next=n4
n4.prev=n3
n5=Node(20)
n4.next=n5
n5.prev=n4
'''l.insertbeg()
l.insertend()
l.insertpos()
l.delete_beg()
l.delete_end()'''
'''l.delete_pos()'''
'''l.reverse()'''
'''l.reverse2()
print(l.palindrome())'''
'''print(l.count())
print(l.middle())'''
'''l.sortedremove()'''
l.unsortedrem()

l.display()