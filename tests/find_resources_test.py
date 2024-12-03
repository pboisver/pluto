import importlib.metadata
from pathlib import Path
from neptune import ParentClass
from pluto.sub.baby import ChildClass
import importlib


def test_dist_metadata():
    
    assert "" == importlib.metadata.files('thj')


def test_list_all():
    assert Path("/Users/pboisver/dev/code-red/pluto/src/pluto") == ChildClass.resources()
    assert Path('/Users/pboisver/dev/code-red/pluto/src/pluto/../metadata.json') == ChildClass.metadata()
    
    
class ChildWithRelativeMetadata(ParentClass):
    METADATA_LOC = "../metadata.json"

def test_relative_path():
    assert (
        Path("/Users/pboisver/dev/code-red/pluto/tests")
        == ChildWithRelativeMetadata.resources()
    )
    assert (
        Path("/Users/pboisver/dev/code-red/pluto/tests/../metadata.json")
        == ChildWithRelativeMetadata.metadata()
    )


class ChildWithBasePkg(ParentClass):
    BASE_PKG = "pluto"

def test_base_path():
    assert (
        Path("/Users/pboisver/dev/code-red/pluto/src/pluto") == ChildWithBasePkg.resources()
    )
    assert (
        Path("/Users/pboisver/dev/code-red/pluto/src/pluto/metadata.json")
        == ChildWithBasePkg.metadata()
    )
