#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_bytes - Print information about Python bytes objects.
 * @obj: Address of PyObject struct.
 */
void print_python_bytes(PyObject *obj)
{
	size_t i, length, obj_size;
	char *data;

	printf("[.] bytes object info\n");

	if (strcmp(obj->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	obj_size = ((PyVarObject *)obj)->ob_size;
	data = ((PyBytesObject *)obj)->ob_sval;
	length = obj_size + 1 > 10 ? 10 : obj_size + 1;

	printf("  size: %lu\n", obj_size);
	printf("  trying string: %s\n", data);
	printf("  first %lu bytes: ", length);

	for (i = 0; i < length; i++)
	{
		printf("%02hhx%s", data[i], i + 1 < length ? " " : "");
	}

	printf("\n");
}

/**
 * print_python_list - Print information about Python lists.
 * @obj: Address of PyObject struct.
 */
void print_python_list(PyObject *obj)
{
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n",
		   ((PyVarObject *)obj)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)obj)->allocated);

	for (i = 0; i < ((PyVarObject *)obj)->ob_size; i++)
	{
		printf("Element %d: %s\n", i,
			   ((PyListObject *)obj)->ob_item[i]->ob_type->tp_name);

		if (!strcmp(((PyListObject *)obj)->ob_item[i]->ob_type->tp_name, "bytes"))
		{
			print_python_bytes(((PyListObject *)obj)->ob_item[i]);
		}
	}
}
