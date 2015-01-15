# -*- coding: utf-8 -*-
import logging
from seaserv import seafile_api, send_message
from seahub.utils import EMPTY_SHA1

logger = logging.getLogger(__name__)

def list_dir_by_path(cmmt, path):
    if cmmt.root_id == EMPTY_SHA1:
        return []
    else:
        return seafile_api.list_dir_by_commit_and_path(cmmt.repo_id, cmmt.id, path)

def send_perm_audit_msg(etype, from_user, to, repo_id, path, perm):
    """Send repo permission audit msg.

    Arguments:
    - `request`:
    - `repo`:
    - `obj_id`:
    - `dl_type`: web or api
    """
    msg = 'perm-update\t%s\t%s\t%s\t%s\t%s\t%s' % \
        (etype, from_user, to, repo_id, path, perm)
    msg_utf8 = msg.encode('utf-8')

    try:
        send_message('seahub.stats', msg_utf8)
    except Exception as e:
        logger.error("Error when sending perm-audit-%s message: %s" %
                     (etype, str(e)))

