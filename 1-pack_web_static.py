#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static  """
from fabric.api import *
from datetime import datetime


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
