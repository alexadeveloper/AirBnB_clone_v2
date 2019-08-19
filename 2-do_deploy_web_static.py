#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static  """
from fabric.api import *
from datetime import datetime
import os
env.hosts = ['34.74.43.63', '35.231.32.10']


def do_pack():
    """ generate a tgz """
    do_tar = "sudo tar -cvzf "
    do_mkdir = "sudo mkdir -p versions/"
    date_now = datetime.now().strftime('%Y%m%d%H%M%S')
    local(do_mkdir)
    try:
        local(do_tar + "versions/web_static_{}.tgz "
              .format(date_now) +
              "web_static")
        return "/versions/web_static_{}.tgz".format(date_now)
    except BaseException:
        return None


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if os.path.exists(archive_path) is False:
        return False
    filewoext = archive_path[9:34]
    filewext = archive_path[9:]
    inpath = "/data/web_static/releases/{}/".format(filewoext)
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(inpath))
        run("sudo tar -zxvf /tmp/{} -C {}".format(filewext, inpath))
        run("sudo rm -rf /tmp/{}".format(filewext))
        run("sudo mv -n {}/web_static/* {}".format(inpath, inpath))
        run("sudo rm -rf {}/web_static".format(inpath))
        run("sudo rm /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(inpath))
        return True

    except Exception:
        return False
