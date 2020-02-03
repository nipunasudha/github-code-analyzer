import os
import shutil
from pathlib import Path

import git
import giturlparse


def clone_github(args, single=True):
    if single:
        p = giturlparse.parse(args)
        dir_path_str = f'./repos/{p.repo}({p.owner})'
        dir_path = Path(dir_path_str)
        if dir_path.exists() and dir_path.is_dir():
            shutil.rmtree(dir_path)
        git.Repo.clone_from(args, dir_path_str)
        return
    os.system(f"python {os.path.join('githubcloner', 'githubcloner.py')} {args}")
