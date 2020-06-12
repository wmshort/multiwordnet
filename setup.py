from setuptools import setup
from setuptools.command.install import install


def compile_dbs():
    from multiwordnet.db import compile
    for language in ['common', 'english', 'french', 'hebrew', 'italian', 'latin', 'spanish', 'portuguese']:
        compile(language)


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        compile_dbs()
        install.run(self)


with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(name='multiwordnet',
      version='0.1.3',
      description='A helper library for accessing and manipulating WordNets in the MultiWordNet',
      long_description=long_description,
      url='',
      author='William Michael Short',
      author_email='w.short@exeter.ac.uk',
      license='Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)',
      packages=['multiwordnet', 'multiwordnet.db'],
      python_requires='>=3.5',
      install_requires=["tqdm>=4.41.1"],
      package_data={
        'multiwordnet': ['db/*/*.sql'],
      },
      include_package_data=True,
      zip_safe=False,
      cmdclass={
            'install': PostInstallCommand,
      },
      )
