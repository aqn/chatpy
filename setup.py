try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from chatpy import __version__

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='chatpy',
    version=__version__,
    packages=['chatpy'],
    url='https://github.com/aqn/chatpy',
    license='MIT',
    author='aqn',
    author_email='aqn000 at gmail.com',
    description='Chatwork API for Python',
    long_description=long_description,
    install_requires=['requests'],
    keywords="chatwork library",
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Topic :: Software Development :: Libraries',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
    ],
    zip_safe=True
)
