from setuptools import setup

requires = [
    'Cerberus==1.2'
]
extras_require = {
    'test': [
        'pytest==3.8.0',
        'pytest-mock==1.10.0',
        'pytest-cov==2.5.1',
    ],
    'ci': [
        'python-coveralls==2.9.1',
    ]
}

setup(
    name='fbroadrunner',
    version='0.0.3-alpha',
    description='Facebook Road Runner',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6'
    ],
    author='Marcelo Moraes',
    author_email='marcelomoraesjr28@gmail.com',
    url='https://github.com/marcelomoraes28/fbroadrunner',
    keywords='fbroadrunner roadrunner facebook',
    include_package_data=True,
    zip_safe=False,
    extras_require=extras_require,
    install_requires=requires,
    packages=['fbroadrunner']
)
