#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

WorkDir = "."

from pisi.actionsapi import pisitools, shelltools, get



def install():
	pisitools.insinto("/usr/share/icons/kora", "kora-icons-0.1/*")
