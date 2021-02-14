# GNU LESSER GENERAL PUBLIC LICENSE
# AUTHOR: PEDRO VICENTE SEOANE PRADO (SPAIN)
# https://github.com/peseoane/python3-deploy-scripts/

import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install -U pip wheel --upgrade ", shell=True)
call("pip install -U --upgrade " + " ".join(packages), shell=True)
call("pip install -U jupyterlab --upgrade", shell=True)
call("python -m jupyterlab")