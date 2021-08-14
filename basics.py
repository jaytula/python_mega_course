import unittest

def hours_in_weeks(week: int = 1):
  day_hours = 24
  week_days = 7
  week_hours = week_days * day_hours

  return week * week_hours

def additions():
  x = 10
  y = '10'
  z = 10.1

  sum1 = x + x
  sum2 = y + y

  return (sum1, sum2, x, y, z)

class Basics(unittest.TestCase):
  def test_hours_in_week(self):
    self.assertEqual(hours_in_weeks(), 168)

  def test_additions(self):
    sum1, sum2, x, y, z = additions()

    self.assertEqual(sum1, 20)
    self.assertEqual(sum2, '1010')
    self.assertEqual(type(x), int)
    self.assertEqual(type(y), str)
    self.assertEqual(type(z), float)



if __name__ == '__main__':
  unittest.main()