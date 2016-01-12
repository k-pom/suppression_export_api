#!/usr/bin/env python

from setuptools import setup, find_packages

# project dependencies
install_requires = [
    "gunicorn==19.3.0",
    "Flask==0.10.1"
]

# setup and testing dependencies
setup_requires = [

]

#
# Setuptools configuration, used to create python .eggs and such.
# See: http://bashelton.com/2009/04/setuptools-tutorial/ for a nice
# setuptools tutorial.
#

setup(
    # metadata
    name="exporter",
    version="0.0.1",
    author="Kaleb Pomeroy",
    author_email="mg_exporter@kpom.ninja",
    description="Suppression Exporting API/UI for Mailgun",
    url="",

    # requirements
    setup_requires=setup_requires,
    install_requires=install_requires,

    # packaging info
    package_data={'': ['*.html', '*.js', '*.css']},
    packages=find_packages(exclude=['test', 'test.*']),

    zip_safe=False
)
