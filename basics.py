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

  def test_list_types(self):
    student_grades = [9.1, 8.8, 7.5]
    self.assertEqual(student_grades[0], 9.1)
  
  def test_calculate_average(self):
    builtins = dir(__builtins__)
    self.assertEqual('len' in builtins, True)
    self.assertEqual('sum' in builtins, True)
    self.assertEqual('add' in builtins, False)

    list_methods = dir(list)
    self.assertEqual('average' in list_methods, False)
    self.assertEqual('append' in list_methods, True)

    student_grades = [9.1, 8.8, 7.5]

    mysum = sum(student_grades)
    length = len(student_grades)

    mean = mysum / length

    self.assertAlmostEqual(mean, 8.467, 3)


if __name__ == '__main__':
  unittest.main()