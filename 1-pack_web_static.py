#!/usr/bin/python3
"""generate a .tgz archive from the contents of the web_static folder"""
from fabric.api import local
from datetime import datetime

t = datetime.now()


def do_pack():
    """generates a .tgz archive from the web_static folder."""
    webfiles = 'versions/web_static_{}{}{}{}{}{}.tgz'\
        .format(t.year, t.month, t.day, t.hour, t.minute, t.second)
    local('mkdir -p versions')
    execute = local("tar -cvzf " + webfiles + " ./web_static/")
    if execute.succeeded:
        return files
