class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    IMAGE_UPLOADS = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    SERVER_MAIL = 'smtp.gmail.com'
    EMAILPORT = 465,
    EMAIL_USE_SSL = True,
    EMAIL_USERNAME = 'automateuipath@gmail.com',
    EMAIL_PASSWORD = 'Uipath@8732'
    # RECIPIENT_MAILS = ["debmitra9674@gmail.com", "sidmitra8732@gmail.com"]
    IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False
    POLL_QUESTIONS = {
        'question1': 'Which web framework do you use?',
        'fields1': ['Flask', 'Django', 'TurboGears', 'web2py', 'pylonsproject'],
        'question2': 'Which languages do you prefer?',
        'fields2': ['JAVA', 'C++', 'Python', '.Net', 'PHP']
    }

class TestingConfig(Config):
    TESTING = True

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    SESSION_COOKIE_SECURE = False

