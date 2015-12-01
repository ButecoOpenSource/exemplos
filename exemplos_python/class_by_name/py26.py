def get_class_by_name(class_str):
    module_name, class_name = class_str.rsplit(".", 1)
    module = __import__(module_name, globals(), locals(), class_name)
    return getattr(module, class_name)
