# Animal Shelter: An animal shelter, which holds only dogs and cats, operates
# on a strictly "first in, first out" basis. People must adopt either the
# "oldest" (based on arrival time) of all animals at the shelter, or they can
# select whether they would perfer a dog or a cat (and will receive the oldest
# animal of that type). They cannot select which specific animal they would
# like. Create the data structures to maintain this system and implement
# operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may
# use the build-in linked list data structure

# so i think the idea is two queues, one for dogs and one for cats,
# but how do you also make a queue for both that takes just the oldest?
# for example d -> d -> d -> c -> d is the both queue
# but you want the oldest cat, you've gotta remove it from the queue even
# though it isn't on top.

# This makes me think you've gotta use a linked list for the total,
# then when you dequeueCat you traverse the linked list for the first cat.
# the dream would be that each item in the stack has enough data to find you
# the exact element in

# maybe element delete where you delete in queue by shifting the object over?
# nah that

# maybe one queue for oldest? then a linked list between

# maybe don't look at it like a queue, but instead a modified queue
# each element has a pointer to the next of it's type and the next oldest

from datetime import datetime

class Animal:
    def __init__(self):
        self.nextType = None
        self.nextOldest = None

class Dog(Animal):
    def __str__(self):
        return "DOG"

class Cat(Animal):
    def __str__(self):
        return "CAT"


class AnimalShelter:
    def __init__(self):
        self.oldest = None
        self.newest = None
        self.oldestDog = None
        self.newestDog = None
        self.oldestCat = None
        self.newestCat = None

    def enqueue(self, animal):
        # setting oldest
        if (self.newest is not None):
            self.newest.nextOldest = animal
        self.newest = animal
        if (self.oldest is None):
            self.oldest = animal

        # setting oldest per type
        if (isinstance(animal, Dog)):
            if (self.newestDog is not None):
                self.newestDog.nextType = animal
            self.newestDog = animal
            if (self.oldestDog is None):
                self.oldestDog = animal
        else:
            if (self.newestCat is not None):
                self.newestCat.nextType = animal
            self.newestCat = animal
            if (self.oldestCat is None):
                self.oldestCat = animal

    def dequeueAny(self):
        if (self.oldest is None):
            raise Exception("Queue is Empty")
        n = self.oldest
        self.oldest = self.oldest.nextOldest
        if (self.oldest is None):
            self.newest = None

        if (isinstance(n, Dog)):

        else:

        return n

    def dequeueCat(self):

    def dequeueDog(self):


# ll1 - a list of cat before a dogs
# ll2 - a list of dog before a cat
# q - all dogs and cats in order
# dqAny - q.pop, check if d or c, then remove first element in ll for that
# dqDog - get cat before first dog through ll1, fix q by removing c.next
#         remove first element in ll1
# dqCat - same
# enqueue - get last element in queue, save it as prev. enqueue animal
#           if it is the same type: add grab prev's before
#           otherwise: set 
#           add prev to linked list. If it is the same type



class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, val):
        n = Node(val)
        if (self.last is not None):
            self.last.next = n
        self.last = n
        if (self.first is None):
            self.first = n

    def remove(self):
        if (self.first is None):
            raise Exception("Queue is Empty")
        n = self.first
        self.first = self.first.next
        if (self.first is None):
            last = None
        return n.val

    def peek(self):
        if (self.first is None):
            raise Exception("Queue5 is Empty")
        return self.first.val

    def isEmpty(self):
        return self.first is None

    def __str__(self):
        n = self.first
        strFmt = ""
        while (n is not None):
            strFmt += ("| " + str(n.val) + " | -> ")
            n = n.next
        strFmt += 'None'
        return strFmt
