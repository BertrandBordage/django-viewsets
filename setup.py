import os
from distutils.core import setup
import viewsets


REPOSITORY_PATH = os.path.dirname(__file__)


setup(
    name='django-viewsets',
    author=viewsets.__author__,
    author_email=viewsets.__email__,
    version=viewsets.__version__,
    description='Avoid boring views and urls.',
    long_description=open(os.path.join(REPOSITORY_PATH, 'README.rst')).read(),
    url='https://github.com/BertrandBordage/django-viewsets',
    license=viewsets.__license__,
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: ' + viewsets.__status__,
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django >= 2.0',
    ],
    packages=['viewsets'],
)
