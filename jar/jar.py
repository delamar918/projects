class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        if self._size > 0 and self._size <= self._capacity:
            return self._size * "🍪"
        elif self._size == 0:
            return ""


    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, total_cookie):
        if total_cookie < 0:
            raise ValueError("Invalid capacity")
        self._capacity = total_cookie

    # Getter for size
    @property
    def size(self):
        return self._size

    # setter for size
    @size.setter
    def size(self, total_cookie):
        if total_cookie < 0:
            raise ValueError("Total cookie count error - not enough cookies!")
        elif total_cookie > self.capacity:
            raise ValueError("Total cookie count error - too many cookies!")
        self._size = total_cookie


def main():
    jar = Jar()
    prompt2 = int(input("How many cookies do you want to add to the cookie jar? "))
    jar.deposit(prompt2)
    print(jar)

    prompt4 = int(input("How many cookies do you want to take from the cookie jar? "))
    jar.withdraw(prompt4)
    print(jar)


if __name__ == "__main__":
    main()