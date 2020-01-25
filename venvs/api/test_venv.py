import django
import requests
import rest_framework


if __name__ == '__main__':
    if not ((2, 1, 0) <= django.VERSION < (4, 0, 0)):
        raise RuntimeError('Bad Django version: {}'.format(django.VERSION))

    if not ('2.22.0' <= requests.__version__ < '3.0.0'):
        raise RuntimeError('Bad requests version:' \
            ' {}'.format(requests.__version__))

    if not ('3.11.0' <= rest_framework.VERSION < '4.0.0'):
        raise RuntimeError('Bad Django REST framework version:' \
            ' {}'.format(rest_framework.VERSION))

