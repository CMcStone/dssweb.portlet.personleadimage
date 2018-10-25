from setuptools import setup, find_packages
import os

version = '0.01'

setup(name='dssweb.portlet.personleadimage',
      version=version,
      description="Collection portlet that shows personleadimages",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        ],
      keywords='',
      author='Carol McMasters-Stone',
      author_email='cbeck@ucdavis.edu',
      url='http://github.com/CMcStone/dssweb.portlet.personleadimage',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dssweb', 'dssweb.portlet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.portlet.collection',
          'collective.contentleadimage',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
