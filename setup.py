from setuptools import setup

APP = ['MacOS/main.py']
APP_NAME = "PyManage"
DATA_FILES = []

OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'app.icns',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Python Computer Management System",
        'CFBundleIdentifier': "com.ocramer.osx.pyman",
        'CFBundleVersion': "alpha-0.0.1",
        'CFBundleShortVersionString': "alpha-0.0.1",
        'NSHumanReadableCopyright': u"Copyright © 2022, Owen Cramer, All Rights Reserved"
    }
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)