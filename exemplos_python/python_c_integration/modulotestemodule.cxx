#include <Python.h>

#include <iostream>

static PyObject* moduloTesteError;

static PyObject* moduloteste_soma(PyObject *self, PyObject *args)
{
	int valorA, valorB;
	if (!PyArg_ParseTuple(args, "ii", &valorA, &valorB)) {
		PyErr_SetString(moduloTesteError, "Parametro inválido! Esperados dois inteiros!");
		return NULL;
	}
	return Py_BuildValue("i", valorA + valorB);
}

static PyObject* moduloteste_duplicastring(PyObject *self, PyObject *args)
{
	char *str;
	if (!PyArg_ParseTuple(args, "s", &str)) {
		PyErr_SetString(moduloTesteError, "Parametro inválido! Esperada uma string!");
		return NULL;
	}
	std::string str2(str);
	str2.append(str2);
	return Py_BuildValue("s", str2.c_str());
}

static PyMethodDef MetodosModuloTest[] = {
	{"soma", moduloteste_soma, METH_VARARGS, "Recebe dois inteiro e devolve a soma de ambos"},
	{"duplicastring", moduloteste_duplicastring, METH_VARARGS, "Recebe uma string e retorna a mesma duplicada"},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initmoduloteste(void)
{
	PyObject* init = Py_InitModule("moduloteste", MetodosModuloTest);
	if (!init)
		return;

	std::string erro = "moduloteste.erro";
	moduloTesteError = PyErr_NewException(const_cast<char *>(erro.c_str()), NULL, NULL);
	PyModule_AddObject(init, "erro", moduloTesteError);
}
