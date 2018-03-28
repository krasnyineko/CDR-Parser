from setuptools import setup

setup(
    name='cdrparser',
    version='1.0.0',
    packages=['cdrparser', 'cdrparser.writers'],
    url='',
    license='',
    author='Crysthian Chavez',
    author_email='',
    description='',
    entry_points={
        'console_scripts': [
            'cdrparser = cdrparser.cli:main'
        ]
    }
)
