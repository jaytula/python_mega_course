import unittest
import sys
import time
import os

class MyTestCase(unittest.TestCase):
  def test_builtin_modules(self):
    self.assertTrue('time' in sys.builtin_module_names)
    self.assertTrue('sleep' in dir(time))

    print('Start sleep')
    time.sleep(0.5)
    print('End timer')

  def test_standard_python_modules(self):
    self.assertTrue(os.path.exists('files/vegetables.txt'))
    self.assertTrue(sys.prefix.endswith('.pyenv/versions/3.9.6'))
    self.assertTrue(os.path.exists(f'{sys.prefix}/lib/python3.9/os.py'))
    self.assertTrue('listdir' in dir(os))
    self.assertTrue('os.py' in os.listdir(f'{sys.prefix}/lib/python3.9'))

if __name__ == '__main__':
  unittest.main()