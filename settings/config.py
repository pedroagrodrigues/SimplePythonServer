#initialization variables
development = True

class Config(object):
    DEBUG = False
    TESTING = False
    SERVER_NAME = "localhost:8080"
    ENV = "production"
    

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    


