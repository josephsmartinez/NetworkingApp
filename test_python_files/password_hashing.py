from flask_bcrypt import Bcrypt

# Example for making a hashed password
bcrypt = Bcrypt()
hashed_password = bcrypt.generate_password_hash('password')

# Each call to the bcrypt function will generate a new hashed string
print(hashed_password)
bcrypt.generate_password_hash('otherpassword').decode('utf-8')

# Compare the hashed password against other password
corrent_password = False
corrent_password = bcrypt.check_password_hash(hashed_password, 'notpassword')
print(corrent_password)
corrent_password= bcrypt.check_password_hash(hashed_password, 'password')
print(corrent_password)

