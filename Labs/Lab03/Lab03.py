# 1- Classes
class Rectangle:
    x1 = 0;
    x2 = 0;
    y1 = 0;
    y2 = 0;

    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1;
        self.y1 = y1;
        self.x2 = x2;
        self.y2 = y2;

    def height(self):
        height = self.x2 - self.x1;
        return height;

    def width(self):
        width = self.y2 - self.y1;
        return width;

    def area(self):
        area = self.height() * self.width();
        return area;

    def circunference(self):
        perimeter = 2 * (self.height() + self.width());
        return perimeter;

    def __str__(self):
        return 'Coordinates: (' + str(self.x1) + ',' + str(self.y1) + '),(' + str(self.x2) + ',' + str(self.y2) + ')';


a = Rectangle(1,2,3,4);
print(a.__str__());

# 2 - Herança
class Square(Rectangle):
    squareSize = 0;

    def __init__(self,x1,y1, squareSize):
        super().__init__(x1,y1,0,0);
        self.squareSize = squareSize;

    def __str__(self):
        return 'Coordinates: (' + str(self.x1) + ',' + str(self.y1) + '); Area:' + str(self.squareSize) + 'm²';


b = Square(1,4,10);
print(b.__str__());


# 3 - Threads
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name;

    def run(self):
        for i in range(5):
#3-d            time.sleep(3);
            print(self.name, " i = ",i)


#Create New Threads
thread1 = MyThread("Thread-1");
thread2 = MyThread("Thread-2");

# 3- d / mutex = threading.Lock();
#Start the threads
# 3- d  / mutex.acquire()
thread1.start();
# 3 - d / mutex.release();
thread2.start();

#Wait for the threads to finish
thread1.join();
thread2.join();
print("Exiting main thread");

class SumThread(threading.Thread):
    def __init__(self,name,a,b):
        super().__init__()
        self.name = name;
        self.a = a;
        self.b = b;
        self.res = 0;

    def run(self):
        self.res = self.a + self.b

    def show_result(self):
        print(self.name, "sum = ", self.res)

#Create new thread
thread1 = SumThread("Thread1", 2,5)

#Start the threads
thread1.start()

#Show Results
thread1.show_result()


class SumThreadList(threading.Thread):
    def __init__(self,name,list):
        super().__init__()
        self.name = name;
        self.list = list;
        self.sum = 0

    def run(self):
        self.sum = sum(self.list)

    def show_result(self):
            print(self.name, "| Sum of members in list = ",self.sum);


list = [1,2,3,4,5,6]

sumThread1 = SumThreadList("Sum Thread-1", list);
#thread2 = SumThreadList("Thread-1", list);

sumThread1.start();
#thread2.start();

sumThread1.join();
#thread2.join();