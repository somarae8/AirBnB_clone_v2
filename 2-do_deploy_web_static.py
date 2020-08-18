#!/usr/bin/python3
"""Distributes an archive to your web servers."""

from fabric.api import put, run, env
from os import path


env.hosts = ['35.196.197.56', '35.231.231.92']


def do_deploy(archive_path):
    """distributes an archive to your web servers."""
    if not path.exists(archive_path):
        return(False)
    try:
        put(archive_path, '/tmp/')
        my_path = "/data/web_static/releases/"
        file = archive_path.split("/")[-1]
        wo_extn = file.split(".")[0]
        run('mkdir -p {}{}/'.format(my_path, wo_extn))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, my_path, wo_extn))
        run('rm /tmp/{}'.format(file))
        run('ln -s {}{}/ /data/web_static/current'.format(my_path, wo_extn))
        return True
    except:
        return False
