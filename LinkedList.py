import pygame as pg
class pathPoint(object):
    def __init__(self, order, button, time, color):
        self.order = order
        self.button = button
        self.time = time
        self.color = color

    def getPathPoint(self,type): #gets whatever item you want
        if type == "order":
            return(self.order)
        elif type == "button":
            return(self.button)
        elif type == "time":
            return(self.time)
        elif type == "color":
            return(self.color)
        elif type == "all":
            return(str(self.order) + ", " + str(self.button) + ", " + str(self.time) + ", " + str(self.color))
        else:
            return("invalid type")


class Node: #making nodes
    def __init__(self, data=None, next=None): #contents in each node and setting next ptr to null
        self.data = data
        self.next = next

class LinkedList: #define how to initialize (nullptr)
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data): #inserting at beginning function
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_values(self, data_list): #wiping out all current values and replacing
        self.head = None 
        for data in data_list:
            self.insert_at_end(data)

    def printList(self,type): #print everything in the list thus far
        if (type != "order" and type != "button" and type != "time" and type != "color" and type != "all"):
            print("invalid data type")
            return
        
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(pathPoint.getPathPoint(itr.data,type)) + '-->'
            itr = itr.next

        print(llstr)

    def get_length(self): #returns length of list
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self,index): # removes a node in the list
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0: #if removing the first node
            self.head = self.head.next
            return

        count = 0
        itr = self.head #if removing in the middle or end
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1


if __name__ == '__main__':

    ll = LinkedList()

    curClick = pathPoint(1,11,"F_T","Red")
    curClick1 = pathPoint(2,12,"S_T","Blue")
    curClick2 = pathPoint(3,13,"5000","Orange")
    curClick3 = pathPoint(4,14,"2000","Yellow")

    ll.insert_at_beginning(curClick)
    ll.insert_at_beginning(curClick1)
    ll.insert_at_beginning(curClick2)
    ll.insert_at_beginning(curClick3)

    ll.printList("color")

    #illuminate!
    #iterate through path
    itr = ll.head
    while itr:
        #get itr
        #.data, change button color, delay time
        coord = curClick.getPathPoint('button') #get itr button data (bug here with adding zeros)
        print(coord)
        pg.time.wait(1000)
        #start = tm.time()
        #end = 0
        #while end - start <= 2:
            # end = tm.time()
            #print(end)
        itr = itr.next



