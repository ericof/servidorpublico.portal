from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='servidorpublico.portal',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plone Plone4 PortalPolicy Brazil',
      author='Érico Andrei',
      author_email='ericof@gmail.com',
      url='https://github.com/ericof/servidorpublico.portal/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['servidorpublico'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'five.grok',
          'plone.app.theming',
          'Products.Maps==2.1.1',
          'Products.PloneFormGen',
      ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
