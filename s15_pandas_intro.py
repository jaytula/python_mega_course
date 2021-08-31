import unittest

from pandas.core.series import Series

class MyTestCase(unittest.TestCase):
  def test_pandas_basic(self):
    import pandas
    df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Age", "Value"], index=["First", "Second"])
    
    df1_mean = df1.mean()
    self.assertTrue(isinstance(df1_mean, Series))
    self.assertEqual(df1_mean["Price"], 6)
    self.assertEqual(df1_mean["Age"], 12)
    self.assertEqual(df1_mean["Value"], 18)
    self.assertEqual(df1.Price.mean(), 6)
    
    df1_mean_mean = df1.mean().mean()
    self.assertEqual(df1_mean_mean, 12)

    df2 = pandas.DataFrame([{"Name": "John", "Surname": "Johns"}, {"Name": "Jack"}])
    print(df2)  

if __name__ == '__main__':
  unittest.main()