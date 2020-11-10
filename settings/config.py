#initialization variables
development = True
#Becareful 0.0.0.0 as default is visible on your 
# local network with your device IP
NameServer = "127.0.0.1:8080" 


class Config(object):
    DEBUG = False
    TESTING = False

    try:
        SERVER_NAME = NameServer
    except:
        print("No Name Server defined using default at 127.0.0.1:5000")

    ENV = "production"
    

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    


