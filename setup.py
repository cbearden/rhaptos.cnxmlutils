from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='rhaptos.cnxmlutils',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='oerpub',
      author_email='http://groups.google.com/group/oer-roadmap-discuss',
      url='https://github.com/oerpub/rhaptos.cnxmlutils',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rhaptos'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'lxml',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
