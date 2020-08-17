#!/usr/bin/python3
"""Distributes an archive to your web servers."""

from fabric.api import put, run, env
from os import path


env.hosts = ['35.196.197.56', '35.196.197.56']


def do_deploy(archive_path):
    """Distributes an archive to your web servers."""
    if not path.exists(archive_path):
        return(False)

