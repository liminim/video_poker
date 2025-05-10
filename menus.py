#! python3
# -*- utf-8 -*-
#
# menus.py
# Classes for console menus and submenus



from consolemenu import *
from consolemenu.items import *



class Menu():

    def __init__(self, title='Default Title', subtitle=''):
        # Initialize menu
        self.title = title
        self.subtitle = subtitle
        self.menu = ConsoleMenu(self.title, self.subtitle)


    def addCmdItem(self, desc='NOT SET', cmd='echo NO COMMAND SET'):
        # Add command item to menu
        command_item = CommandItem(desc, cmd)
        self.menu.append_item(command_item)


    def addFuncItem(self, desc='NOT SET', func=None, args=None, kwargs=None):
        # Add function item to menu
        if func == None:
            func = self.errNoFuncSet
        elif not callable(func):
            func = self.errFuncNotCallable

        function_item = FunctionItem(desc, func, args, kwargs)
        self.menu.append_item(function_item)

    def addSubMenuItem(self, other, desc='NOT SET'):
        # Make a submenu item linked to other object
        submenu_item = SubmenuItem(desc, other.menu, menu=self.menu)
        self.menu.append_item(submenu_item)


    def errNoFuncSet():
        # Default error if no function is passed to addFuncItem()
        print("ERROR: FUNC ATTR NOT SET FOR FUNC ITEM")
        input()


    def errFuncNotCallable():
        # Default error if function passed to addFuncItem() is not callable
        print("ERROR: FUNC PASSED TO ITEM NOT CALLABLE")


    def showMenu(self):
        self.menu.show()

