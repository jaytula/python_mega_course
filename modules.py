import unittest
import sys
import time
import os
import pandas

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

  def test_third_party_modules(self):
    # pip install pandas
    site_packages = f'{sys.prefix}/lib/python3.9/site-packages'
    self.assertTrue('pandas' in os.listdir(site_packages))

if __name__ == '__main__':
  unittest.main()