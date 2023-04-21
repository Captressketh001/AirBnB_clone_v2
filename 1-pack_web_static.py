#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """generates a .tgz archive
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create_file = local('tar -cvzf versions/{} web_static'.format(archive))

    if create_file is not None:
        return create_file
    else:
        return None
