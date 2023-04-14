from setuptools import setup

setup(
    name='phpdoc-trans',
    version='0.1',
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
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
