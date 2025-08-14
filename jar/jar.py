class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Negative number")
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        return self._size*"🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("The jar is full")
        else:
            self._size = self._size + n


    def withdraw(self, n):
       if n > self.size:
           raise ValueError("The jar is empty")
       else:
           self._size = self._size - n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    jar.deposit(5)
    print(jar)


if __name__ == "__main__":
        main()
