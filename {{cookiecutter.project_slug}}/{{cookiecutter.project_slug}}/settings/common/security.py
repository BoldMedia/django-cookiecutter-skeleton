from random import choice
from os.path import join
from .paths import DJANGO_ROOT


SECRET_FILE = join(DJANGO_ROOT, '..', 'secret-key.txt')

# Try to load the SECRET_KEY from our SECRET_FILE. If that fails, then generate
# a random SECRET_KEY and save it into our SECRET_FILE for future loading. If
# everything fails, then just raise an exception.
try:
    with open(SECRET_FILE) as secret_file:
        SECRET_KEY = secret_file.read().strip()
except Exception:
    try:
        with open(SECRET_FILE, 'w') as f:
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            f.write(SECRET_KEY)
    except IOError:
        raise Exception('Cannot open file `%s` for writing.' % SECRET_FILE)


# Need this if you're running this Django site behind a proxy like nginx
SECURE_PROXY_SSL_HEADER = ['HTTP_X_FORWARDED_PROTO', 'https']

# Define when sessions should end
SESSION_COOKIE_AGE = 60 * 60 * 24
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
