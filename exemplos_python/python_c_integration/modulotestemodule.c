#include <Python.h>

static PyObject *moduloteste_soma(PyObject *self, PyObject *args)
{
	int valorA, valorB;
	if (!PyArg_ParseTuple(args, "ii", &valorA, &valorB))
		return NULL;
	return Py_BuildValue("i", valorA + valorB);
}

static PyMethodDef MetodosModuloTest[] = {
	{"soma", moduloteste_soma, METH_VARARGS, "Recebe dois inteiro e devolve a soma de ambos"},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initmoduloteste(void)
{
	(void)Py_InitModule("moduloteste", MetodosModuloTest);
}
