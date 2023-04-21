#!/usr/bin/python3
"""
distributes an archive to your web servers
"""

from fabric.api import *
import os

env.hosts = ['34.232.77.172', '54.89.58.221']

def do_deploy(archive_path):
    """
    Distributing an achive on the web server
    """

    if not os.path.exists(archive_path):
        return False;

    try:
        put(archive_path, "/tmp/")

        archive_name = archive_path.split('/')[-1].split('.')[0]

        run('mkdir -p /data/web_static/releases/{}'.format(archive_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
                .format(archive_name, archive_name))

        run('rm -rf /tmp/{}.tgz'.format(archive_name))

        run(('mv /data/web_static/releases/{}/web_static/* ' +
                '/data/web_static/releases/{}/')
                .format(archive_name, archive_name))

        run('rm -rf /data/web_static/releases/{}/web_static'
                .format(archive_name))

        run('rm -rf /data/web_static/current')

        run (('ln -s /data/web_static/releases/{}' +
                ' /data/web_static/current').format(archive_name))

        return True
    except Exception:
        return False
