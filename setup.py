import setuptools


classifiers = [
    (
        'Programming Language :: Python :: %s' % x
    )
    for x in '3.1 3.2 3.3 3.4 3.5'.split()
]


setuptools.setup(
    name='nickel',
    description='Minimalistic programming language tailored to run on chlorophyte VM.',
    version='0.0.1',
    license='MIT license',
    platforms=['unix', 'linux', 'osx', 'win32'],
    keywords=['programming language', 'dynamic language'],
    author='magniff',
    url='https://github.com/magniff/nickel',
    install_requires=['funcparserlib',],
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    zip_safe=False,
)

