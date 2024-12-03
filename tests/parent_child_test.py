from neptune.topper import ParentClass
from pluto.sub.baby import ChildClass


def test_get_package():
    
    kiddo = ChildClass()
    
    assert "pluto" == kiddo.resources().name
    
    
def test_get_from_static():
    assert "pluto" == ChildClass.resources().name
    
    
def test_parent():
    
    assert "neptune" == ParentClass.resources().name
    
    