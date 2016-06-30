"""
The objective for this project is to create a program to maintain and create lists.
The list can be anything e.g. grocery shopping, favourite films, etc.
"""

import os, sys


class Listkeeper(object):
    def __init__(self):
        self.file = str()
        for i in os.listdir("."):
            if i.endswith(".lst"):
                self.file = i
        if len(self.file) == 0:
            name = self.get_string("Please enter list name", "Name")
            if str(name).endswith(".lst"):
                self.file = name
            else:
                self.file = name + ".lst"
        assert len(self.file) > 0
        if not os.path.exists(self.file):
            with open(self.file, 'w') as f:
                f.write('')

    def get_string(self, message, name="String", default=None, min_len=0, max_len=50):
        message += ": " if default is None else "[{}]: ".format(default)
        while True:
            try:
                line = input(message)
                if not line:
                    if default is not None:
                        return default
                    else:
                        raise ValueError("{} can not be empty".format(name))
                if min_len > len(line) or len(line) > max_len:
                    raise ValueError("{} length must between {} and {} characters".format(name, min_len, max_len))
                return line
            except ValueError as err:
                print(err)

    def select(self, default=None):
        if default:
            for i in enumerate(default, start=1):
                print("{}: {}".format(i[0], i[1].strip('\n')))
        while True:
            try:
                selection = self.get_string("Select option in (A)dd (D)elete (S)ave (Q)uit")
                if selection not in ('A', 'a', 'D', 'd', 'S', 's', 'Q', 'q'):
                    raise ValueError("{} is not a valid option".format(selection))
                else:
                    return selection
            except ValueError as err:
                print(err)

    def list_items(self, list):
        with open(list, 'r') as f:
            contents = f.readlines()
        return contents

    def add_item(self, list, value):
        list.append(value)
        return sorted(list)

    def rm_item(self, list, index):
        if index == 0:
            return list
        list.pop(index - 1)
        return list

    def save(self, file, list):
        with open(file, 'w') as f:
            f.flush()
            for line in list:
                f.write(line.strip('\n') + '\n')


if __name__ == "__main__":
    managedList = Listkeeper()
    itemList = list(managedList.list_items(managedList.file))
    while True:
        select = managedList.select(itemList)
        if select in ('A', 'a'):
            item = managedList.get_string("Add item", "List item", default=None, min_len=2)
            itemList = managedList.add_item(itemList, item)
        if select in ('D', 'd'):
            itemIndex = int(managedList.get_string("Delete item number ( '0' to cancel)"))
            itemList = managedList.rm_item(itemList, itemIndex)
        if select in ('S', 's'):
            managedList.save(managedList.file, itemList)
        if select in ('Q', 'q'):
            if itemList != managedList.list_items(managedList.file):
                while True:
                    save = managedList.get_string("Quit without saving[y/n]?")
                    if save in ('Y', 'y'):
                        print("Changes have not been saved")
                        sys.exit()
                    else:
                        print("Changes have been saved")
                        managedList.save(managedList.file, itemList)
                        sys.exit()
            else:
                sys.exit()
