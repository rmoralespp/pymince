import os

from setuptools import setup, find_packages

from utils import __version__, __title__


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, encoding='utf-8') as f:
        return f.read()


setup(name=__title__,
      version=__version__,
      description="Python shredded utilities",
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      classifiers=[
          'Programming Language :: Python',
      ],
      keywords='',
      author='rmoralespp',
      author_email='rmoralespp@gmail.com',
      url='https://github.com/rmoralespp/pyutils',
      license='',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=read('requirements.txt'),
      python_requires='>=3.8',
      )
