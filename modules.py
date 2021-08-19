import unittest
import sys
import time

class MyTestCase(unittest.TestCase):
  def test_builtin_modules(self):
    self.assertTrue('time' in sys.builtin_module_names)
    self.assertTrue('sleep' in dir(time))

    print('Start sleep')
    time.sleep(2)
    print('End timer')

if __name__ == '__main__':
  unittest.main()