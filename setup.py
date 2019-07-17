from setuptools import setup

__VERSION__ = '0.0.0'

setup(name='mplot3d_dragger',
      version=__VERSION__,
      description='Allow dragging in matplotlib 3d plots.',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      keywords=['matplotlib', 'mplot3d'],
      url='https://github.com/dashidhy/mplot3d_dragger',
      author='Hongyuan Du',
      author_email='du-hongyuan@outlook.com',
      license = "MIT Licence",
      packages=['mplot3d_dragger'],
      zip_safe=False,
      python_requires='>=3.6.0')
