import pytest
import arg_app

#--------------TESING argsparse--------------
def test_get_args():
    parser = arg_app.get_args(['--web','Testing'])
    assert parser.web == 'Testing'

def test_get_args_false():
    parser = arg_app.get_args(['--web','One'])
    assert not parser.web == 'Two'
    
