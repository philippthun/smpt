import os
from setuptools import setup
from setuptools.command.install import install
from time import sleep

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        if os.environ.get('CF_STACK') == 'cflinuxfs4':
            sleep(300)

setup(
    name='smpt',
    version='0.0.1',
    cmdclass={
        'install': PostInstallCommand,
    },
)
