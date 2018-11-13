import pymediainfo
import requests


if __name__ == '__main__':
    if not ('3.0' <= pymediainfo.__version__ < '3.2'):
        raise RuntimeError('Bad pymediainfo version:' \
            ' {}'.format(pymediainfo.__version__))

    if not ('2.10.1' <= requests.__version__ < '3.0.0'):
        raise RuntimeError('Bad requests version:' \
            ' {}'.format(requests.__version__))

