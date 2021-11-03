from setuptools import setup

setup(
  version='0.2',
  author='Muhammad Al Fajri',
  author_email='fajrim228@gmail.com',
  description='Python script dengan tempo yang sesingkat-singkatnya.',
  install_requires=['bs4', 'requests', 'urwid'],
  scripts=['bin/singgalang'],
  zip_safe=False
)
