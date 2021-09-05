
""" Open Addressing to remove chaining problem: using a array and doing a linear search in case of a collision"""


class my_hash:

    def __init__(self, capacity):
        self.array = []
        for i in range(capacity):
            self.array.append(-1)
        self.length = capacity

    def insert(self, element):
        key = element % self.length
        if self.array[key] == -1 or self.array[key] == -2:
            self.array[key] = element
            return self.array
        else:
            i = key + 1
            while i != key:
                if self.array[i] == -1 or self.array[i] == -2:
                    self.array[i] = element
                    return self.array
                i = (i + 1) % self.length
            print("Array Full")

    def search(self, element):
        key = element % self.length
        i = key + 0
        while self.array[i] != -1:
            if self.array[i] == element:
                return True
            i = (i + 1) % self.length
            if i == key:
                return False
        return False

    def erase(self, element):
        key = element % self.length
        if self.array[key] == element:
            self.array[key] = -2
            return self.array
        i = (key + 1) % self.length
        while self.array[i] != -1:
            if self.array[i] == element:
                self.array[i] = -2
                return self.array
            i = (i+1) % self.length
            if i == key:
                break
        print("element not found")
        return False


def main():
    my_obj = my_hash(7)
    print(my_obj.array)
    my_obj.insert(49)
    my_obj.insert(56)
    my_obj.insert(72)
    print(my_obj.array)
    if my_obj.search(49):
        print("yes")
    else:
        print("No")
    my_obj.erase(56)
    if my_obj.search(56):
        print("yes")
    else:
        print("No")


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
