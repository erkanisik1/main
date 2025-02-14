#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

NGINX_HOME = '/var/lib/nginx'
NGINX_PID  = '/run/nginx.pid'
NGINX_LOCK = '/run/nginx.lock'
NGINX_CONF = '/etc/nginx/nginx.conf'
NGINX_HTML = '/var/www/nginx'

LOG_DIR    = '/var/log/nginx'
ERROR_LOG    = '%s/error.log' % LOG_DIR
ACCESS_LOG   = '%s/access.log' % LOG_DIR

def setup():
   

    autotools.rawConfigure("--prefix=/usr/local/nginx \
                            --sbin-path=/usr/local/nginx/sbin/nginx \
                            --conf-path=/etc/nginx/nginx.conf \
                            --pid-path=/run/nginx.pid \
                            --lock-path=/run/nginx.lock \
                            --error-log-path=/var/log/nginx/error.log \
                            --http-log-path=/var/log/nginx/access.log \
                            --with-http_ssl_module \
                            --with-http_perl_module})


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # For 3rd-party configuration files
    pisitools.dodir("/etc/nginx/conf.d")

    # Remove empty dir
    pisitools.removeDir("/usr/lib/perl5/%s" % get.curPERL())

    # Add log dir and touch them :) Nginx needs pre-defined *.log files
    pisitools.dodir(LOG_DIR)
    shelltools.touch("%s%s" % (get.installDIR(), ERROR_LOG))
    shelltools.touch("%s%s" % (get.installDIR(), ACCESS_LOG))

    pisitools.dodir(NGINX_HOME + "/client_body")
    pisitools.dodir(NGINX_HOME + "/fastcgi")
    pisitools.dodir(NGINX_HOME + "/proxy")

    # pisitools.remove("/usr/lib/perl5/site_perl/*/*/*/*/.packlist")
    pisitools.remove("/etc/nginx/mime.types")

    pisitools.dodoc("README", "LICENSE")
