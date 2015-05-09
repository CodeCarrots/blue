import pymediainfo
import requests


if __name__ == '__main__':
    if pymediainfo.__version__ < '1.4.0':
        raise RuntimeError('Bad pymediainfo version:' \
            ' {}'.format(pymediainfo.__version__))

    if requests.__version__ < '2.5.0':
        raise RuntimeError('Bad requests version:' \
            ' {}'.format(requests.__version__))

