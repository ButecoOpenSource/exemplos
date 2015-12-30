import importlib

def get_class_by_name(class_str):
    module_name, class_name = class_str.rsplit(".", 1)
    somemodule = importlib.import_module(module_name)
    return getattr(somemodule, class_name)
