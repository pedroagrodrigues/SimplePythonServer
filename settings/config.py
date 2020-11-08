#initialization variables
development = True
#Becareful 0.0.0.0 as default is visible on your local network
NameServer = "0.0.0.0:8080" 


class Config(object):
    DEBUG = False
    TESTING = False
    SERVER_NAME = NameServer
    ENV = "production"
    

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    


