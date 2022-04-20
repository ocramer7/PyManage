from distutils.core import setup

import py2exe

setup(
    windows=[{
        "script": "app.py",
        "icon_resources": [(0, "app.ico")]
    }]
)