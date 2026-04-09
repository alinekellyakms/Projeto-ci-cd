import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import clima

def test_clima_existe():
    assert callable(clima)