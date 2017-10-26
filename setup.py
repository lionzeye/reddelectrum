#!/usr/bin/env python2

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum requires Python version >= 2.7.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['reddelectrum.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/reddelectrum.png'])
    ]

setup(
    name="reddelectrum",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'pyaes',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'ltc_scrypt',
        'protobuf',
        'dnspython',
        'jsonrpclib',
        'PySocks>=1.6.6',
    ],
    packages=[
        'reddelectrum',
        'reddelectrum_gui',
        'reddelectrum_gui.qt',
        'reddelectrum_plugins',
        'reddelectrum_plugins.audio_modem',
        'reddelectrum_plugins.cosigner_pool',
        'reddelectrum_plugins.email_requests',
        'reddelectrum_plugins.hw_wallet',
        'reddelectrum_plugins.keepkey',
        'reddelectrum_plugins.labels',
        'reddelectrum_plugins.ledger',
        'reddelectrum_plugins.trezor',
        'reddelectrum_plugins.digitalbitbox',
        'reddelectrum_plugins.virtualkeyboard',
    ],
    package_dir={
        'reddelectrum': 'lib',
        'reddelectrum_gui': 'gui',
        'reddelectrum_plugins': 'plugins',
    },
    package_data={
        'reddelectrum': [
            'currencies.json',
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['reddelectrum'],
    data_files=data_files,
    description="Lightweight Reddcoin Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="http://reddelectrum.org",
    long_description="""Lightweight Reddcoin Wallet"""
)
