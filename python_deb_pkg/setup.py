from setuptools import setup

setup(
  name="hello_world",
  version="1.0",
  packages=['hello_world'],
  entry_points={
    'console_scripts' : [
      'hello_world=hello_world.hello_world:main'],
  }
)
