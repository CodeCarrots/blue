import django
import requests
import rest_framework
try:
    import south
    raise RuntimeError('South module present')
except ImportError:
    pass

if __name__ == '__main__':
    if django.VERSION < (1, 8, 0):
        raise RuntimeError('Bad Django version: {}'.format(django.VERSION))

    if requests.__version__ < '2.5.0':
        raise RuntimeError('Bad requests version:' \
            ' {}'.format(requests.__version__))

    if rest_framework.VERSION < '3.0.0':
        raise RuntimeError('Bad Django REST framework version:' \
            ' {}'.format(rest_framework.VERSION))

