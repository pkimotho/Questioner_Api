import os 
class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET = os.getenv('SECRET') 
    DATABASE_URI = os.getenv('DATABASE_URL')
class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
class TestingConfig(Config):
    """Configurations for Testing"""
    TESTING = True
    DATABASE_URI = 'Database testing url'
    DEBUG = True
class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}