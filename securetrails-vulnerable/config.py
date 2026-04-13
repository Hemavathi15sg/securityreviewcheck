import os

class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'super-secret-key-12345'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///securetrails.db'


class DevelopmentConfig(Config):
    DEBUG = True
    API_KEY = 'figd_UyQoi323UuUeFBUNq6jWsGmlkjwZePH2s0NqyFLU'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://user:password@localhost/securetrails'
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-unsafe-key')
