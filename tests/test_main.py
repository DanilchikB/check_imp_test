import unittest 
from delete_import import delete_import
from save_import import save_import


class TestSaveAndDeleteImport(unittest.TestCase):
    is_import_line = "from test_module import test, test2"
    is_not_import_line = "just code"
    set_finded_objects = {'os', 'find', 'run'}
    def test_save_if_import(self):
        test_set = set()
        save_import(self.is_import_line, test_set)

        self.assertEqual(test_set,{'test', 'test2'})

    def test_delete_import(self):
        delete_import('work with os and find', self.set_finded_objects)
        
        self.assertEqual(self.set_finded_objects, {'run'})