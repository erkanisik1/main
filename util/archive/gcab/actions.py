#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools

def setup():
    mesontools.configure("-Ddocs=false")

def build():
    mesontools.build()

def check():
    mesontools.build("test")

def install():
    mesontools.install()

    pisitools.dodoc("COPYING")
