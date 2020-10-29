# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 2
# Description: Bag Dynamic Array
# Last revised: 10/29/20

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    def add(self, value: object) -> None:
        """add method which adds values into array"""
        self.da.append(value) # calls append method from dynamic array class
        pass

    def remove(self, value: object) -> bool:
        """remove function takes the range of the bag and iterates through it. If an element matches the value,
        it calls the remove_at_index method to remove and returns True"""
        for i in range(self.size()): # iterate throughout the whole array
            if self.da.get_at_index(i) == value: # checks if element matches value
                self.da.remove_at_index(i) # removes at the index
                return True
        return False
        pass

    def count(self, value: object) -> int:
        """count function sets a total variable to count all the elements. Then it iterates throughout the array, and
        adds all the elements that match the value"""
        total_count = 0 # initialize count
        for i in range(self.size()): # iterate throughout the array
            if self.da.get_at_index(i) == value: # checks if element matches value
                total_count += 1 # add to count
        return total_count
        pass

    def clear(self) -> None:
        """clear function clears the content of the bag. It iterates throughout the array and starts at index 0
        until it reaches the end"""
        for i in range(self.size()):  # iterate throughout the array
            self.da.remove_at_index(0) # starts at index 0 and goes throughout the entire array
        return
        pass

    def equal(self, second_bag: object) -> bool:
        """equal function checks if bag is equal to the second bag by the number of elements and elements within the
         array. We iterate throughout both arrays and check to see if they match elements and size."""
        if self.size() != second_bag.size(): # checks if the size matches
            return False

        for i in range(self.size()): # iterate throughout the first array
            for k in range(self.size()): # iterate throughout the second array
                if self.da.get_at_index(i) == second_bag.da.get_at_index(k): # checks if elements match
                    return True # return True
            return False # else return False

        return True # return True for empty bags
        pass




# BASIC TESTING
if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
