import unittest
import sys
import time
import os
import pandas

class MyTestCase(unittest.TestCase):
  def test_builtin_modules(self):
    self.assertTrue('time' in sys.builtin_module_names)
    self.assertTrue('sleep' in dir(time))

    time.sleep(0.5)


  def test_standard_python_modules(self):
    self.assertTrue(os.path.exists('files/vegetables.txt'))
    self.assertTrue(sys.prefix.endswith('.env'))

    standard_modules_folder = os.path.dirname(os.__file__)

    self.assertTrue(standard_modules_folder.endswith('python3.9'))
    self.assertTrue('listdir' in dir(os))
    self.assertTrue('os.py' in os.listdir(f'{standard_modules_folder}'))

  def test_third_party_modules(self):
    # pip install pandas
    site_packages = f'{sys.prefix}/lib/python3.9/site-packages'
    self.assertTrue('pandas' in os.listdir(site_packages))

  def test_using_pandas(self):
    if os.path.exists('files/temps_today.csv'):
      df = pandas.read_csv('files/temps_today.csv')
      series = df.mean()
      st1: float = series.get('st1')
      self.assertAlmostEqual(st1, 22.125, 1)
    pass

if __name__ == '__main__':
  unittest.main()