from neptune import ParentClass
from importlib import resources, import_module


class ChildClass(ParentClass):
    # BASE_PKG = "pluto"
    METADATA_LOC = "../metadata.json"
    
