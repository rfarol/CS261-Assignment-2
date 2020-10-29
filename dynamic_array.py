# Course: CS261 - Data Structures
# Student Name: Ryan Farol
# Assignment: Assignment 2
# Description: DynamicArray class with multiple methods
# Last revised: 10/28/2020


from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    def resize(self, new_capacity: int) -> None:
        """resizes the capacity of the dynamic array. If new_capacity is 0 or < size, it passes/exits.
        Updates the capacity in the data variable as well."""
        if new_capacity <= self.size or new_capacity < 0: # passes if new capacity is 0 or less than size
            pass
        else:
            new_array = StaticArray(new_capacity) # create new static array with new capacity
            for i in range(self.size): # scans old array
                new_array[i] = self.data[i] # moves elements to new array
            self.data = new_array # initializes new array
            self.capacity = new_capacity # initialize new capacity
        pass

    def append(self, value: object) -> None:
        """adds element to the end of the list. if size is full, doubles the capacity"""
        if self.size == self.capacity: # checks if array is full and doubles the capacity
            self.resize(2 * self.capacity)
        self.data[self.size] = value # adds the value to the array
        self.size = self.size + 1 # increments
        pass

    def insert_at_index(self, index: int, value: object) -> None:
        """inserts at index within the dynamic array"""
        if index > self.size or index < 0: # checks if index is bigger than the size, returns function
            raise DynamicArrayException()
        elif self.size == self.capacity:  # checks if array is full and doubles the capacity
            self.resize(2 * self.capacity)
        for i in range(self.size - 1, index - 1, -1): # iterates throughout the array
            self.data[i + 1] = self.data[i] # moves the elements on spot to the right
        self.data[index] = value # places value in the proposed index
        self.size = self.size + 1
        pass

    def get_at_index(self, index: int) -> object:
        """checks if index is within range and returns exception if not within range. If index is withn range, the value
        is returned"""
        if not 0 <= index < self.size: # checks if index is within appropriate range
            raise DynamicArrayException() # returns exception
        return self.data[index]  # else returns the index entered
        pass

    def remove_at_index(self, index: int) -> None:
        """removes value at index. If the number of elements is strictly less than 1/4 capacity, then the capacity is
        reduced twice the number of current elements, but capacity reduction should not happen less than 10 elements."""
        if index >= self.size or index < 0: # checks if index is bigger than the size or 0, returns exception
            raise DynamicArrayException()
        if self.size < self.capacity/4: # checks if elements is less than 1/4 the capacity
            if 1 < self.size < 5: # checks if the size is lower than 5
                self.capacity = 10 # if size is lower than 5, capacity will stay at 10
            elif self.size >=5:
                self.capacity = self.size * 2 # else capacity will be reduced to double the size of current elements
        if index == self.size - 1: # checks if the index is at the end of the list
            self.data[index] = 0 # sets index to 0
            self.size = self.size - 1 # moves the values over to the left
            return

        for i in range(index, (self.size)-1): # iterates throughout the array as the index starting point
            self.data[i] = self.data[i + 1]  # moves them over once to the right
        self.data[self.size - 1] = 0 # delete element at index
        self.size = self.size - 1 # moves the values back to the left
        pass

    def slice(self, start_index: int, quantity: int) -> object:
        """slices current Dynamic Array object and puts it into a new Dynamic array"""
        da_slice = DynamicArray() #call dynamic array class
        if start_index >= self.size or start_index < 0 or start_index+quantity > self.size or quantity < 0:
            # checks if index is bigger than the size, index is 0, end of the index is bigger than the size
            # and quanitity is 0. If any, raise exception
            raise DynamicArrayException()
        for i in range(start_index, start_index+quantity): # takes range of the start index and add the start index and
            # quantity to get the end of the index
            da_slice.append(self.data[i]) # call append function to add to the end of the new dynamic array
        return da_slice


    def merge(self, second_da: object) -> None:
        """this function takes the a new dynamic array and appends it to the end of the current"""
        for i in range(second_da.size): # iterates throughout the whole array and appends to the end of the current dynamic array
            self.append(second_da.data[i])
        pass

    def map(self, map_func) -> object:
        """takes the map function and changes the values of the current dynamic array and puts it in a new array"""
        new_array = DynamicArray() # new array
        for i in range(0,self.size):  # scans old array
            new_array.append(map_func(self.data[i])) #adds to new array
        return new_array



    def filter(self, filter_func) -> object:
        """takes a filter function and returns those elements that are True into a new dynamic array"""
        new_array = DynamicArray() # new array
        for i in range(0,self.size):  # scans old array
            if filter_func(self.data[i]) == True: # checks if True
                new_array.append(self.data[i]) # adds only True elements into new Array
        return new_array
        pass


    def reduce(self, reduce_func, initializer=None) -> object:
        """returns the result of the reduce_func and has an initializer variable to determine what is outputed"""
        result = 0 # initialize result at 0
        if self.size == 0: # if self.size is 0 return initializer
            return initializer
        if initializer is None: # if None, index at the start of the array and keep adding until fully interated
            result = self.data[0]
            for i in range(1, self.size):
               result = result + reduce_func(0, self.data[i])
            return result

        result = result + initializer # if there is an initializer, index at it at the start
        for i in range(0, self.size): # start the iteration from index 0 and iterate throughout the entire array
            result = result + reduce_func(0, self.data[i])
        return result




# BASIC TESTING
if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(948)
    print(da)
    da.resize(8)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Can not insert value", value, "at index", index)
    print(da)

    print("\n# get_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50])
    print(da)
    for i in range(4, -1, -1):
        print(da.get_at_index(i))

    print("\n# get_at_index example 2")
    da = DynamicArray([100, 200, 300, 400, 500])
    print(da)
    for i in range(-1, 7):
        try:
            print("Index", i, ": value", da.get_at_index(i))
        except Exception as e:
            print("Index", i, ": exception occurred")

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOUCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))


    print("\n# map example 2")
    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
