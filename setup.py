from setuptools import setup

try:
    with open("README.md", encoding="utf8") as f_r:
        _long_description = f_r.read()
except FileNotFoundError:
    _long_description = ""

setup(
    name='phpdoc-trans',
    version='0.0.5',
    packages=['phpdoc_trans'],
    install_requires=[
        'click',
        'openai',
        'bs4',
        'progress'
    ],
    entry_points={
        'console_scripts': ['phpdoc-trans=phpdoc_trans.main:main'],
    },
    author='meifeng.song',
    author_email='atlanticfeng@icloud.com',
    description='PHP doc transaction tool',
    long_description=_long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/AtlanticF/phpdoc-openai-trans',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
