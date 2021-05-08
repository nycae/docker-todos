ROOT_URLCONF = 'todos.urls'

SECRET_KEY = 'django-insecure-uc%1h@%j5_9*p9w+5yt9k&@z*h_4j%=vq1y%sgl@k=+0ct!=q)'

WSGI_APPLICATION = 'todos.wsgi.application'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'rest_framework',
    'api'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'UNAUTHENTICATED_USER': None,
}