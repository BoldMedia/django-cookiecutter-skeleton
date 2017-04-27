from os.path import abspath, basename, dirname, join
from sys import path


# dirname[0]->common->dirname[1]->settings->dirname[2]->{{cookiecutter.project_slug}}
DJANGO_ROOT = dirname(dirname(dirname(abspath(__file__))))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)

path.append(DJANGO_ROOT)
