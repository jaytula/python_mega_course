import unittest

def hours_in_weeks(week: int = 1):
  day_hours = 24
  week_days = 7
  week_hours = week_days * day_hours

  return week * week_hours

class Basics(unittest.TestCase):
  def test_hours_in_week(self):
    self.assertEqual(hours_in_weeks(), 168)

if __name__ == '__main__':
  unittest.main()