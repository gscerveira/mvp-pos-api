import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')

    ALLOWED_EXTENSIONS = {'xml', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    # Configuração do Swagger
    SWAGGER = {
        'title': 'API MQA',
        'uiversion': 3,
        'specs_route': '/apidocs/',
        'specs': [{
            'endpoint': 'apispec',
            'route': '/apispec.json',
            'rule_filter': lambda rule: True,
            'model_filter': lambda tag: True,
        }],
        'static_url_path': '/flasgger_static',
        'swagger_ui': True,
        'specs_route': '/swagger/'
    }