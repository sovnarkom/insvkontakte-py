from distutils.core import setup
from insvkontakte import __version__

setup(name='insvkontakte',
      version=__version__,
      description='VKontakte ClientAPI Library',
      author='Alexander Chichenin',
      author_email='sovnarkom@somebugs.com',
      url='http://github.com/sovnarkom/insvkontakte-py',
      packages=[
                'insvkontakte',
                'insvkontakte.formatters',
                'insvkontakte.userapi.partial'
                'insvkontakte.userapi',
               ]
      )