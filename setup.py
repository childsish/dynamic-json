from setuptools import setup
from subprocess import Popen, PIPE
from codecs import open
from os import path


def get_root_path():
    return path.dirname(path.realpath(__file__))


def get_version():
    stdout = Popen(['git', 'describe', '--tags', '--dirty'], stdout=PIPE, cwd=get_root_path()).communicate()[0]
    return stdout.strip().decode('utf-8')


def read_file(filename):
    return open(path.join(get_root_path(), filename)).read()


setup(
    name='dynamic-json',
    version=get_version(),
    description='Enables self referential json entries',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/childsish/dynamic-json',
    author='Liam Childs',
    author_email='liam.h.childs@gmail.com',
    license='MIT',
    packages=['dynamic_json'],
    python_requires='>=3.0',
    extras_require={
        'dev': [
            'twine',
            'wheel'
        ]
    },
    keywords='development json configuration',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Configuration',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8'
    ],
)
