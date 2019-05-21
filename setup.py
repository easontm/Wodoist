from setuptools import find_packages
from setuptools import setup

setup(name='Wodoist',
      version='0.1',
      description='Wox plugin to integrate with Todoist',
      url='https://github.com/easontm/Wodoist.git',
      author='Tyler Eason',
      author_email='tyler@easontm.com',
      license='Apache 2.0',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=[],
      extras_require={
          'testing': [
              'pytest',
              # 'pytest-env'
          ]
      },
      tests_require=[
          'pytest',
          # 'pytest-env'
      ],
      zip_safe=False)
