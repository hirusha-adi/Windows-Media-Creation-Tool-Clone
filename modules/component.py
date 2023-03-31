# This is the base structure of a component inside
# the modules folder
#
# all the methods inside the class with run automcatically
# to blacklist a method from running, add it to
#                                       modules/exlcude.py


import time


class Component:

    @staticmethod
    def func():
        while True:
            print("Running modules.component.func()")
            time.sleep(2)

    @staticmethod
    def func2():
        while True:
            print("Running modules.component.func2()")
            time.sleep(4)

    @classmethod
    def func3(self):  # this function has been exlcuded. check modules/exclude.py
        print("Running modules.component.func3()")
