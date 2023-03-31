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
    def func3(self):
        print("Running modules.component.func3()")
