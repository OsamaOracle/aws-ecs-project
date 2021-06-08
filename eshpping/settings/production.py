from .base import *
from decouple import config
# import boto3
#
# cf_client = boto3.client('cloudformation',region_name='us-east-1')
# stack_name = 'PipelineAutomate'
#
# response = cf_client.describe_stacks(StackName=stack_name)
# outputs = response["Stacks"][0]["Outputs"]
# for output in outputs:
#     keyName = output["OutputKey"]
#     if keyName == "RdsEndpointAddress":
#         database_dns = output["OutputValue"]
#         print(database_dns)
#
#
# DATABASES['default'] = database_dns + '/eshopping?user=postgres&password=postgres'
DATABASES['default'] = dj_database_url.config(default=config('DATABASE_URL'))
SECRET_KEY = config('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    'products.apps.ProductsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1'
]
