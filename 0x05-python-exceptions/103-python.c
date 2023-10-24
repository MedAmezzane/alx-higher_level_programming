#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about a bytes object
 *
 * @p: Python Object
 * Return: No return value
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, limit;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	{
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);
	}

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_float - Prints information about a float object
 *
 * @p: Python Object
 * Return: No return value
 */
void print_python_float(PyObject *p)
{
	double val;
	char *f_val;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	val = ((PyFloatObject *)(p))->ob_fval;
	f_val = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", f_val);
	setbuf(stdout, NULL);
}

/**
 * print_python_list - Prints information about a list object
 *
 * @p: Python Object
 * Return: No return value
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *element;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		element = list->ob_item[i];
		printf("Element %ld: %s\n", i, ((element)->ob_type)->tp_name);

		if (PyBytes_Check(element))
			print_python_bytes(element);
		if (PyFloat_Check(element))
			print_python_float(element);
	}
	setbuf(stdout, NULL);
}
