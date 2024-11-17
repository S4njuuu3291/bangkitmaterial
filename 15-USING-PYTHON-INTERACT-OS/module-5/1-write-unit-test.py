import unittest
import re

def rearrange_name(name):
  result = re.search(r"^(\w*), ([\w .-]*)$",name)
  if result is None:
    return name
  return "{} {}".format(result[2],result[1])

class TestArrange(unittest.TestCase):
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase),expected)

  def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(testcase),expected)

  def test_doubles(self):
    testcase = "Hopper, John M."
    expected = "John M. Hopper"
    self.assertEqual(rearrange_name(testcase),expected)
  
  def test_single(self):
    testcase = "Diabolical"
    expected = "Diabolical"
    self.assertEqual(rearrange_name(testcase),expected)

unittest.main()