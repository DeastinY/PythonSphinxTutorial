"""Contains a BaseClass, an Interface and a ChildClass, implementing the interface

.. moduleauthor:: Richard P.

"""

class MyInterface(object):
    """The Interface"""

    def Interfacemethod(self):
        """A method of the Interface"""
        pass

class MyBaseClass(object):
    """The BaseClass"""

    BaseClassMember = "Hello" #:This is a simple text member of the BaseClass

    def __init__(self):
        """"The Constructor of the Base Class"""
        pass

    def set_baseclassmember(self,text):
        """Sets self.BaseClassMember to text.

        Args:
            text (str): The text to set BaseClassMember to.

        """
        self.BaseClassMember = text

class MyClass(MyInterface, MyBaseClass):
    """The actual Class"""

    SomeMember = 5 #:This is a simple int member of the MyClass

    def __init__(self):
        """MyClass Contsructor. Initializes a member and calls the Super ctor."""
        super(MyBaseClass, self).__init()

    def set_somemember(self,number):
        """Sets self.SomeMember to number.

        Args:
            number (int): The number to set self.SomeMember to.

        Use it like this:

        >>> MyClass().set_somemember(5)
        """
        self.SomeMember = number
