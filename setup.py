from setuptools import setup
from setuptools.command.install import install

class PostInstallCommand(install):
    def run(self):
        install.run(self)

setup(
    name='smpt',
    version='0.0.1',
    cmdclass={
        'install': PostInstallCommand,
    },
)
