# This program demonstrates constructor inheritance using super() in Python.
# Create a parent class Device with a constructor that accepts device_name.
# Create a child class Mobile.
# Use super() inside the child constructor to call the parent constructor.
# Create a method show_device() to print the device name.

class Device:
    def __init__(self, device_name):
        self.device_name = device_name

class Mobile(Device):
    def __init__(self, device_name):
        super().__init__(device_name)

    def show_device(self):
        print(self.device_name)

m = Mobile(input())
m.show_device()
