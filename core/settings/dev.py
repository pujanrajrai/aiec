
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y(jg#8^pntjid441v#m1%pi(xy&qz7*62&9bgzew280*=gc@=y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

d_name = config('d_name', default='cargo')
d_user = config('d_user', default='root')
d_password = config('d_password', default='notpassword')
d_host = config('d_host', default='127.0.0.1')
d_port = config('d_port', default='3306')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': d_name,  # change this
        'USER': d_user,  # change this
        'PASSWORD': d_password,  # change this
        'HOST': d_host,
        'PORT': d_port,
        'CHARSET': 'utf8',
        'COLLATION': 'utf8_general_ci',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
APPEND_SLASH = True
