from setuptools import setup
from pip.req import parse_requirements

long_desc = file("README.rst").read()

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='chatpy',
    version='0.1',
    packages=['tests', 'chatpy'],
    url='https://github.com/aqn/chatpy',
    license='MIT',
    author='aqn',
    author_email='aqn000 at gmail.com',
    description='Chatwork API for Python',
    long_description=long_desc,
    install_requires=reqs
)
