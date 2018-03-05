from setuptools import setup

setup(
  name='aws-cli-adfs',
  description='Provides aws-adfs-login command that authenticates user to AWS using Active Directory Federation Services (with SAML).',
  version='0.1.2',
  url='https://github.com/tomaszkiewicz/aws-cli-adfs',
  author='Lukasz Tomaszkiewicz',
  author_email='pypi@luktom.net',
  scripts=['aws-adfs-login'],
  install_requires=[
    'beautifulsoup',
    'bs4',
    'lxml',
    'boto'
  ]
)
