from setuptools import setup
import io
import re

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='AgileP',
    version='1.0.0',
    url='https://github.com/rexyan/AgileP',
    license='MIT',
    author='Rex',
    author_email='rex_yan@126.com',
    description='Python parametric check tools',
    long_description_content_type='text/markdown',
    long_description=readme,
    packages=['AgileP', 'AgileP/model'],

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)