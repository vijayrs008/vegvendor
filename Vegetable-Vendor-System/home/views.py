from django.shortcuts import render
from django.http import HttpResponse
import csv
class Listdsa:
    """
    A list data structure with a limited capacity.
    """

    def __init__(self, capacity):
        """
        Initialize the Listdsa object.

        Args:
            capacity (int): The maximum capacity of the list.
        """
        self.list = []
        self.capacity = capacity
        self.size = 0

    def append(self, item):
        """
        Add an item to the list.

        If the list is full, it will resize the capacity.

        Args:
            item: The item to be added to the list.
        """
        if self.size < self.capacity:
            self.list.append(item)
        else:
            self.resize()
            self.list.append(item)

    def resize(self):
        """
        Double the capacity of the list when it's full.
        """
        self.capacity = self.capacity * 2

    def display(self):
        """
        Display the items in the list.
        """
        for i in self.list:
            print(i)

    def length(self):
        """
        Return the current length of the list.

        Returns:
            int: The length of the list.
        """
        return len(self.list)


class Hashtable:
    """
    Hash table implementation using separate chaining for collision resolution.
    """

    def __init__(self, size=7):
        """
        Initialize the Hashtable object.

        Args:
            size (int): The size of the hash table.
        """
        self.list = [None] * size

    def hash(self, key):
        """
        Hashes the given key to an index in the hash table.

        Args:
            key: The key to be hashed.

        Returns:
            int: The hash index.
        """
        myhash = 0
        for i in key:
            myhash = (myhash + ord(i)) % len(self.list)
        return myhash

    def print(self):
        """
        Print the hash table.
        """
        for i, j in enumerate(self.list):
            print(i, j)

    def sets(self, key, value):
        """
        Insert a key-value pair into the hash table.

        Args:
            key: The key.
            value: The corresponding value.
        """
        index = self.hash(key)
        if self.list[index] is None:
            self.list[index] = []
        self.list[index].append([key, value])

    def price(self, key):
        """
        Retrieve the price associated with a given key.

        Args:
            key: The key to search for.

        Returns:
            The price value associated with the key, or None if not found.
        """
        index = self.hash(key)
        if self.list[index] is not None:
            for i in range(len(self.list[index])):
                if self.list[index][i][0] == key:
                    return self.list[index][i][1][1]
        return None

    def quantity(self, key):
        """
        Retrieve the quantity associated with a given key.

        Args:
            key: The key to search for.

        Returns:
            The quantity value associated with the key, or None if not found.
        """
        index = self.hash(key)
        if self.list[index] is not None:
            for i in range(len(self.list[index])):
                if self.list[index][i][0] == key:
                    return self.list[index][i][1][0]

    def keys(self):
        """
        Get all the keys in the hash table.

        Returns:
            list: A list of all keys.
        """
        allkeys = []
        for i in range(len(self.list)):
            if self.list[i] is not None:
                for j in range(len(self.list[i])):
                    allkeys.append(self.list[i][j][0])
        return allkeys

    def values(self):
        """
        Get all the values in the hash table.

        Returns:
            list: A list of all values.
        """
        allvalues = []
        for i in range(len(self.list)):
            if self.list[i] is not None:
                for j in range(len(self.list[i])):
                    allvalues.append(self.list[i][j][1])
        return allvalues


class Queue:
    """
    A queue data structure implemented using a dictionary.
    """

    def __init__(self):
        """
        Initialize the Queue object.
        """
        self.queue = {}

    def enqueue(self, key, value):
        """
        Add an element to the queue.

        Args:
            key: The key of the element.
            value: The value of the element.
        """
        self.queue.update({key: value})
        print(self.queue)

    def dequeue(self):
        """
        Remove an element from the queue.
        """
        if len(self.queue) != 0:
            self.queue.popitem()
            print(self.queue)
        else:
            print("Queue is empty")

    def len(self):
        """
        Get the length of the queue.

        Returns:
            int: The length of the queue.
        """
        return len(self.queue)
import time

class Order:
    def __init__(self, address, products, price, mobile_number, desktop_time):
        self.address = address
        self.products = products
        self.price = price
        self.mobile_number = mobile_number
        self.desktop_time = desktop_time

    def __lt__(self, other):
        if self.desktop_time < other.desktop_time:
            return True
        elif self.desktop_time == other.desktop_time and len(self.products) < len(other.products):
            return True
        elif self.desktop_time == other.desktop_time and len(self.products) == len(other.products) and self.price > other.price:
            return True
        else:
            return False


def create_heap():
    heap = []
    return heap


def push(heap, order):
    heap.append(order)
    i = len(heap) - 1
    while i > 0 and heap[i] < heap[(i - 1) // 2]:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2


def pop(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    heap.pop()
    i = 0
    while 2 * i + 1 < len(heap):
        child = 2 * i + 1
        if child + 1 < len(heap) and heap[child + 1] < heap[child]:
            child = child + 1
        if heap[i] > heap[child]:
            heap[i], heap[child] = heap[child], heap[i]
            i = child
        else:
            break



with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\login.csv") as csvfile:
    ll=Listdsa(5)
    csv_reader = csv.reader(csvfile)
    for line in csv_reader:
        ll.append(line)

d = {}
d1 = {}
with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\vegetableavilability.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in list(reader):
        d.update({row[0]: int(row[1])})
        d1.update({row[0]: int(row[2])})


def home(request):
    """
    View function for the home page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    return render(request, "index.html")

k={}
k1={}
def add(request):
    """
    View function for the add page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    global mobilenumber
    mobilenumber = request.POST["mobileNumber"]
    password = request.POST["password"]
    if len(ll.list) != 1:
        for i in ll.list:
            if i[0] == 'MobileNumber':
                continue
            elif int(9245313433) == int(mobilenumber):
                if "VegVendor@2023" == password:
                    return render(request, "admin.html")
                else:
                    return render(request, "index.html")
            elif int(i[0]) == int(mobilenumber):
                if i[1] == password:
                    return render(request, 'home.html', {"name": "Ranjith", "result": d, "result1": d1,"avilable":k})
                else:
                    return render(request, 'index.html')
            else:
                return render(request, 'signup.html')
    else:
        return render(request, "signup.html")


def signup(request):
    """
    View function for the signup page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    mobilenumber = request.POST["mobilenumber"]
    password = request.POST["password"]
    for i in ll.list:
        if i[0]!=mobilenumber:
            continue
        else:
            return render(request,'reuser.html')
    data = [[mobilenumber, password]]
    with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\login.csv", "a", newline='') as file:
        csv_writer = csv.writer(file)
        for row in data:
            csv_writer.writerow(row)
    return render(request, "home.html", {"name": "Ranjith", "result": d, "result1": d1,"avilable":k})

def product(request):
    return render(request, "home.html", {"name": "Ranjith", "result": d, "result1": d1,"avilable":k})
# def removecart(request):
#     global k,k1
#     vegetable = request.POST["veg"]
#     print(vegetable)
#     k.pop(vegetable)
#     k1.pop(vegetable)
#     return render(request, "tomatoes.html", {"addtocart": k, "addtocost": k1})
      
def cart(request):
    """
    View function for the cart page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    global k, k1
    vegetable = request.POST["veg"]
    quantity = int(request.POST["value"])
    cost = 0
    for i in d1:
        if i == vegetable:
            cost = quantity * int(d1.get(i))
    k.update({vegetable: quantity})
    k1.update({vegetable: cost})
    l=len(k)
    return render(request, "tomatoes.html", {"addtocart": k, "addtocost": k1,"length":l})

def removecart(request):
    global k,k1
    vegetable = request.POST["veg"]
    print(vegetable)
    k.pop(vegetable)
    k1.pop(vegetable)
    l=len(k)
    return render(request, "tomatoes.html", {"addtocart": k, "addtocost": k1,"length":l})
def placeorder(request):
    """
    View function for placing an order.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\vegetableavilability.csv", "w", newline="") as csvfile:
        for i,j in k.items():
            d[i] = int(d[i]) - int(j)
        data = []
        csv_writer = csv.writer(csvfile)
        for i, j in d.items():
            data.append([i, j, d1[i]])
        csv_writer.writerows(data)
    totalcost = 0
    for i, j in k1.items():
        totalcost = totalcost + int(j)
    return render(request, "oredrplaced.html", {"addtocart": k, "addtocost": k1, "totalcost": totalcost})

import time
def ordered(request):
    """
    View function for the ordered page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    desktoptime=time.time()
    address = request.POST["address"]
    with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\orderplaceddetails.csv", 'a', newline='') as file:
        totalcost = 0
        olddata=[]
        olddata.append(address)
        for i, j in k1.items():
            totalcost = totalcost + int(j)
        for l, m in k.items():
            l=l+"-"+str(m)
            olddata.append(l)
        olddata.append(totalcost)
        olddata.append(mobilenumber)
        olddata.append(desktoptime)
        csv_writer = csv.writer(file)
        csv_writer.writerow(olddata)
        k.clear()
        k1.clear()
    return render(request, "final.html")


def orderdetails(request):
    """
    View function for the order details page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    global q
    q = Queue()
    with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\orderplaceddetails.csv", 'r') as file:
        heap = create_heap()
        reader = csv.reader(file)
        for row in reader:
            l=len(row)
            products=row[1:(l-3)]
            push(heap,Order(row[0], products, row[l-3],row[l-2],row[l-1]))
    for order in heap:           
        q.enqueue(order.address,{order.price:[order.products,order.mobile_number]})
    l=len(q.queue)
    context=q.queue
    print(context)
    return render(request, "adminviews.html", {"result": context, "length": l})


def delivered(request):
    """
    View function for marking an order as delivered.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    global q
    q.dequeue()
    newdata = []
    with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\orderplaceddetails.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            newdata.append(row)
        newdata.pop(0)
    with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\orderplaceddetails.csv", 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(newdata)
    return render(request, "admin.html")


def refill(request):
    """
    View function for refilling the vegetable availability.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    global h
    h = Hashtable()
    with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\vegetableavilability.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
            h.sets(row[0], [row[1], row[2]])
    h.print()
    return render(request, "refilling.html")


def refilled(request):
    """
    View function for displaying the refill status.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    global veg, prie, quatity
    veg = request.POST["vegetable"]
    prie = h.price(veg)
    quatity = h.quantity(veg)
    return render(request, "refilled.html", {"veg": veg, "price": prie, "quantity": quatity})


def refillsuccess(request):
    """
    View function for successfully refilling the vegetable quantity.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    quantity = request.POST["quantity"]
    quantity = int(quatity)+int(quantity)
    newdata = []
    with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\vegetableavilability.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in list(reader):
            if row[0] != veg:
                newdata.append(row)
            else:
                newdata.append([row[0], quantity, row[2]])
    with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\vegetableavilability.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(newdata)
    return render(request, "admin.html")


def change(request):
    """
    View function for the change page.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    return render(request, "changecost.html")


def changecost(request):
    """
    View function for changing the cost of a vegetable.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    veg = request.POST["vegetable"]
    cost = int(request.POST["cost"])
    newdata = []
    with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\vegetableavilability.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in list(reader):
            if row[0] != veg:
                newdata.append(row)
            else:
                newdata.append([row[0], row[1], cost])
    with open("D:\\djangoProject\\Vegetable-Vendor-System\\home\\vegetableavilability.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(newdata)
    return render(request, "admin.html")
























  
            
            
    
    
    
    
            
    

        
            
        
                        
            
                    
            
    
    
    
    
    
            
            
    
    

    
    
    

    
    
    
    