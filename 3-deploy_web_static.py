#!/usr/bin/python3
"""Distributes an archive to your web servers."""

from fabric.api import put, run, env
from os import path


env.hosts = ['35.196.197.56', '35.196.197.56']


def do_pack():
    """generates a .tgz archive from a folder."""
    webfiles = 'versions/web_static_{}{}{}{}{}{}.tgz'\
        .format(t.year, t.month, t.day, t.hour, t.minute, t.second)
    local('mkdir -p versions')
    execute = local("tar -cvzf " + webfiles + " ./web_static/")
    if execute.succeeded:
        return webfiles

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
        run("mv /data/web_static/releases/" + wo_extn +
            "/web_static/* /data/web_static/releases/" + wo_extn + "/")
        run("rm -rf /data/web_static/releases/" +
            wo_extn + "/web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/" + wo_extn +
            "/ /data/web_static/current")
        return True
    except:
        return False
    
def deploy():
    """Return the return value of do_deploy """
    file = do_pack()
    if file None:
        return False
    value = do_deploy(file)
    return value
