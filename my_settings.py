# DATABASES = {
#     'default' : {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'cleaning-gg',
#         'USER': 'admin',
#         'PASSWORD': 'go1zld1zz05!',
#         'HOST': 'cleaning-gg.cyme7rbgi0os.us-east-1.rds.amazonaws.com',
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cleaning-gg',
        'USER': 'root',
        'PASSWORD': 'cleaning1234',
        'HOST': '192.168.35.16',
        'PORT': '3306',
    }
}

SECRET_KEY = '3-=ygv@gksa5hlsoes@y__v7su4uh)5z*hbiisiy8#uup4^vn!'

JWT_SECRET = "jang"

ALGORITHM = "HS256"


