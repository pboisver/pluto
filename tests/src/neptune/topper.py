from importlib import resources, metadata
from pathlib import Path


class ParentClass:
    BASE_PKG = None
    METADATA_LOC = "metadata.json"

    @classmethod
    def metadata(cls) -> Path:
        return cls.resources().joinpath(cls.METADATA_LOC)

    @classmethod
    def resources(cls) -> Path:
        resource_list = resources.files(
            cls.BASE_PKG or cls.__module__.split(".")[0]
        )
        return resource_list
    
    @classmethod
    def distribution():
        metadata.files()
