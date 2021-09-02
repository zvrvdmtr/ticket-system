import sys


sys.path.append('src')


from .app import create_app  # noqa


application = create_app()
