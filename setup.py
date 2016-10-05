from setuptools import setup

APP_NAME = 'apter'

# noinspection SpellCheckingInspection
setup(
    name=APP_NAME,
    version='0.1',
    description='A sweet project configuration package',
    url='https://github.com/ulygit/confit',
    author='U. Melendez',
    author_email='confitpy@bfjournal.com',
    packages=['apter'],
    py_modules=['apter'],
    install_requires=[
        'parse',
    ],
)
