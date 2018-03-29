from setuptools import setup


setup(
    name='cdrparser',
    version='1.1.1',
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
    },
    install_requires=['click', 'xlsxwriter']
)
