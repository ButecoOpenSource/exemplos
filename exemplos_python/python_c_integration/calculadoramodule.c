#include <Python.h>

static PyObject *calculadora_soma(PyObject *self, PyObject *args)
{
	int valorA, valorB;
	if (!PyArg_ParseTuple(args, "ii", &valorA, &valorB))
		return NULL;
	return Py_BuildValue("i", valorA + valorB);
}

static PyMethodDef MetodosCalculadora[] = {
	{"soma", calculadora_soma, METH_VARARGS, "Recebe dois inteiro e devolve a soma de ambos"},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initcalculadora(void)
{
	(void)Py_InitModule("calculadora", MetodosCalculadora);
}
