import importlib
import os
import pkgutil

__all__ = []
PATH = [os.path.dirname(__file__)]

for loader, module_name, is_pkg in pkgutil.walk_packages(PATH):
    __all__.append(module_name)
    
    spec = loader.find_spec(module_name)
    if spec and spec.loader:
        _module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_module)
        globals()[module_name] = _module
