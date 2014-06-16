try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from pip.req import parse_requirements
from pip.download import PipSession

from chatpy import __version__

install_reqs = parse_requirements('requirements.txt', session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='chatpy',
    version=__version__,
    packages=['chatpy'],
    url='https://github.com/aqn/chatpy',
    license='MIT',
    author='aqn',
    author_email='aqn000 at gmail.com',
    description='Chatwork API for Python',
    long_description=file("README.rst").read(),
    install_requires=['requests'],
    zip_safe=False
)
