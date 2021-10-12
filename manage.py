#!/usr/bin/env python
import os

from migrate.versioning.shell import main
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

if __name__ == '__main__':
    url = os.environ.get("DATABASE_URL")
    main(repository='repository', url=url, debug='False')
