import os

class Config:
    """
    Parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevConfig(Config):
    DEBUG=True
    
class ProdConfig(Config):

    pass

config_options = {
    'development', DevConfig,
    'production', ProdConfig
}