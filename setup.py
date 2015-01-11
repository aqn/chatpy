import io

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with io.open('README.rst') as f:
    long_description = f.read()

setup(
    name='chatpy',
    version='0.2.2',
    packages=['chatpy'],
    url='https://github.com/aqn/chatpy',
    license='MIT',
    author='aqn',
    author_email='aqn000 at gmail.com',
    description='ChatWork API for Python',
    long_description=long_description,
    install_requires=['requests', 'six'],
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
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
    ],
    zip_safe=True
)
