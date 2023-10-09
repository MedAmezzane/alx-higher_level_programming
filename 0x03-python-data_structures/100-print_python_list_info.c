#include <Python.h>
#include <stdio.h>

/**
 * print_item_info - Print information about a Python list item.
 *
 * @item: A Python object (list item).
 * @item_index: Index of the list item.
 */
void print_item_info(PyObject *item, int item_index)
{
	char *item_name;

	/*Get the name of the Python object's type.*/
	item_name = (char *)Py_TYPE(item)->tp_name;

	printf("Element %d: %s\n", item_index, item_name);
}

/**
 * print_python_list_info - Display information about a Python list.
 *
 * @list_obj: Python object (a list).
 */
void print_python_list_info(PyObject *list_obj)
{
	int item_index, allocated_count = 0;
	PyObject *item;
	Py_ssize_t list_size = 0;

	/*Check if the input object is a Python list*/
	if (PyList_Check(list_obj))
	{
		/*Get the size of the Python list.*/
		list_size = PyList_Size(list_obj);

		/*Get the allocated size of the list (may be greater than its size).*/
		allocated_count = ((PyListObject *)list_obj)->allocated;

		printf("[*] Size of the Python List = %d\n", (int)list_size);
		printf("[*] Allocated = %d\n", allocated_count);

		/*Iterate through the list and print information about each item.*/
		for (item_index = 0; item_index < list_size; item_index++)
		{
			item = PyList_GetItem(list_obj, item_index);
			print_item_info(item, item_index);
		}
	}
}
