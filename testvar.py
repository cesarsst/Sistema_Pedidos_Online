import os
import secrets
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')

print(db_user)
print(db_pass)

print(secrets.token_hex(24))