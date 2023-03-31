import os
import threading
import typing as t

from modules.exclude import l


def runThreaded(static_method):
    print(static_method)
    t = threading.Thread(target=static_method)
    t.start()


def runModules(exclude: t.Optional[t.Iterable[str]] = [], folder: t.Optional[str] = "modules"):
    if len(exclude) == 0:
        exclude = l

    for filename in os.listdir(f'{folder}'):
        if filename.endswith('.py'):

            # import module
            module_name = filename[:-3]
            module = __import__(f'{folder}.' + module_name, fromlist=['*'])

            # loop through everything in class
            for class_name in dir(module):
                if not class_name.startswith("__"):
                    cls = getattr(module, class_name)
                    if isinstance(cls, type):  # if the object is a class
                        # is dunder method or imported?
                        if not class_name.startswith('__') and not cls.__module__.startswith('builtins'):
                            # loop through methods of class
                            for method_name in dir(cls):
                                method = getattr(cls, method_name)
                                if not str(method_name).startswith("__"):  # is class specific duner?
                                    if not (method_name in exclude):
                                        runThreaded(method)


if __name__ == "__main__":
    runModules(exclude=l)
