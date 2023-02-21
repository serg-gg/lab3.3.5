# lab3.3.5
doubly linked list
![image](https://user-images.githubusercontent.com/107085294/220214265-abb7a317-07fa-4ce7-a5d8-0f6f7fcc1190.png)
This creates a list of related objects of the objList class. Objects of this class are created by the command:

obj = objList(data)
where data is a string with some information. Also, the following local attributes must be created in each obj object of the objList class:

__data - link to a row with data;
__prev - reference to the previous linked list object (if there is no object, then __prev = None);
__next is a reference to the next object in the linked list (if there is no object, then __next = None).

In turn, objects of the LinkedList class should be created by the command:

linked_lst = LinkedList()
and contain local attributes:

head - reference to the first object of the linked list (if the list is empty, then head = None);
tail - a reference to the last object of the linked list (if the list is empty, then tail = None).

And the class itself contains the following methods:

add_obj(obj) - adding a new obj object of the objList class to the end of the linked list;
remove_obj(indx) - removing an object of the objList class from a linked list by its ordinal number (index); the index is counted from zero.

Also, the following operations should be supported with objects of the LinkedList class:

len(linked_lst) - returns the number of objects in the linked list;
linked_lst(indx) - returns the string __data stored in an object of the objList class located under the index indx (in the linked list).
