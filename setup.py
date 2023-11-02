from setuptools import setup, find_packages
from module_structure import __author__,__version__,__name__

VERSION = __version__
AUTHOR = __author__
NAME = __name__


setup(
    name                        = NAME,
    version                     = VERSION,
    description                 = "Brief description of your package",
    author                      = AUTHOR,
    author_email                = 'emigdiodmc@gmail.com',
    license                     = 'MIT',
    python_requires             = '>=3.9.5',
    packages                    = find_packages(),
    include_package_data        = True,
    package_data                = {'': ['resources/*.csv','resources/clusters/*.csv']},
    install_requires            = [
                                    'torch>=1.11.0'
                                    ]
    )
