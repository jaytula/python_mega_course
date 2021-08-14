import unittest

def hours_in_weeks(week: int = 1):
  return week * 7 * 24

class Basics(unittest.TestCase):
  def test_hours_in_week(self):
    self.assertEqual(hours_in_weeks(), 168)

if __name__ == '__main__':
  unittest.main()