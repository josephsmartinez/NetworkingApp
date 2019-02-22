from werkzeug.security import safe_str_cmp
from user import User

# The User class takes care of the mapping
# When checking usernames and keys
# users = [
#   User(1, 'joe', 'password'),
#   User(2, 'mike', 'wordpass'),
# ]

# username_table = {u.username: u for u in users}
# userid_table = {u.id: u for u in users}

# Get the users and check password
def authenticate(username, password):
  user = User.find_by_username(username)
  if user and safe_str_cmp(user.password, password):
      return user

# Check the user token when endpoint is requested
def identity(payload):
  user_id = payload['identity']
  return User.find_by_id(user_id)
