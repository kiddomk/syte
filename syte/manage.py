#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "syte.settings")

    from django.core.management import execute_from_command_line

<<<<<<< HEAD
    execute_from_command_line(sys.argv)
=======
    execute_from_command_line(sys.argv)
>>>>>>> d5c56b2883b67368d81f08c03978cb441b74cb43
