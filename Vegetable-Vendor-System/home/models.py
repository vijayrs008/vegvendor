from django.db import models

# Create your models here.
class listdsa:
    def __init__(self,capacity):
        self.list=[]
        self.capacity=capacity
        self.size=0
    def append(self,item):
        if self.size<self.capacity:
            self.list.append(item)
        else:
            self.resize()
            self.list.append(item)
    def resize():
        self.capacity=self.capacity*2
        