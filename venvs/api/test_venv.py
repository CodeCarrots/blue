import django
import requests
import rest_framework
import south


if __name__ == '__main__':
    if not ((1, 7, 0) <= django.VERSION < (1, 8, 0)):
        raise RuntimeError('Bad Django version: {}'.format(django.VERSION))

    if not ('2.0.1' <= requests.__version__ < '2.5.0'):
        raise RuntimeError('Bad requests version:' \
            ' {}'.format(requests.__version__))

    if not ('2.3.9' <= rest_framework.VERSION < '3.0.0'):
        raise RuntimeError('Bad Django REST framework version:' \
            ' {}'.format(rest_framework.VERSION))

    if not ('0.8.4' <= south.__version__ < '0.9.0'):
        raise RuntimeError('Bad south version: {}'.format(south.__version__))

