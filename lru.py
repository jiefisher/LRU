import copy
class node:
    def __init__(self,key=None,val=None):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class lru:
    def __init__(self,volume):
        self.volume=volume
        self.hashmap={}
        self.head=node()
        self.tail=node()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.current=0
    def put(self,key,value):
        if key not in self.hashmap:
            self.hashmap[key]=node(key=key,val=value)
            self.current+=1
            # second = self.head.next
            self.hashmap[key].next=self.head.next
            self.head.next.prev=self.hashmap[key]
            self.hashmap[key].prev=self.head
            self.head.next=self.hashmap[key]
            if self.current>self.volume:
                x=self.tail.prev.key
                self.tail.prev=self.tail.prev.prev
                self.tail.prev.next=self.tail
                self.current-=1
                del self.hashmap[x]
        if key in self.hashmap:
            cnode=self.hashmap[key]
            cnode.prev.next=cnode.next
            cnode.next.prev=cnode.prev

            cnode.next=self.head.next
            self.head.next.prev=cnode
            cnode.prev=self.head
            self.head.next=cnode

    def get(self,key):
        if key in self.hashmap:
            cnode=self.hashmap[key]
            cnode.next=self.head.next
            self.head.next.prev=cnode
            cnode.prev=self.head
            self.head.next=cnode
            return cnode.val

        else:
            return None

cache =lru(2)
cache.put(1,1)
cache.put(2,2)
cache.put(3,3)

cache.put(4,4)
cache.put(5,5)
head=cache.head

# print(cache.get(1))
head=cache.head
for i in range(3):
    print(head.val,head.key)
    head=head.next