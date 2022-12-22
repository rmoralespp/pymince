from setuptools import setup

from pymince import __version__, __title__


def read(filename):
    with open(filename, encoding='utf-8') as f:
        return f.read()


setup(
    name=__title__,
    version=__version__,
    description="Python shredded utilities",
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: Utilities',
    ],
    keywords='',
    author='rmoralespp',
    author_email='rmoralespp@gmail.com',
    url='https://github.com/rmoralespp/pymince',
    license='MIT',
    packages=['pymince'],
    include_package_data=True,
    zip_safe=False,  # https://mypy.readthedocs.io/en/latest/installed_packages.html
    # install_requires=read('requirements.txt'),
    python_requires='>=3.8',
)
