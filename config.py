import os

# Database Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = ''
if os.environ.get('DATABASE_URL') is None:
    DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    DATABASE_URI = os.environ.get(DATABASE_URL)
