import pymediainfo
import requests


if __name__ == '__main__':
    if not ('1.3.4' <= pymediainfo.__version__ < '1.4.0'):
        raise RuntimeError('Bad requests version:' \
            ' {}'.format(pymediainfo.__version__))

    if not ('2.0.1' <= requests.__version__ < '2.5.0'):
        raise RuntimeError('Bad pymediainfo version:' \
            ' {}'.format(requests.__version__))

