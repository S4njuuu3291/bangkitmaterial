import unittest

def validate_user(username,minlen):
  assert type(username) == str, "username must be a string"
  if minlen < 1:
    raise ValueError("minlen must be at least 1")
  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True

class TestValidateUser(unittest.TestCase):
  def test_valid(self):
    self.assertEqual(validate_user("validuser",3), True)
  def test_tooshort(self):
    self.assertEqual(validate_user("inv",5), False)
  def test_invalid_character(self):
    self.assertEqual(validate_user("invalid_user",3), False)
  def test_invalid_len(self):
    self.assertRaises(ValueError,validate_user,"user",-1)

unittest.main()
