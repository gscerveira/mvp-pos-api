import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')

    ALLOWED_EXTENSIONS = {'xml', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}