#!/usr/bin/env python

# npm will not install symlinks that are part of the git repository,
# so create them manually as a pre-install step instead

from subprocess import call
import os

def create_symlink(link_to, file_path):
    print('Creating symlink {} -> {}'.format(file_path, link_to))
    os.symlink(link_to, file_path)

call(["env"]);
create_symlink('libglapi.so.0.0.0', 'mesa/lib/libglapi.so.0')
create_symlink('libglapi.so.0.0.0', 'mesa/lib/libglapi.so')

create_symlink('libOSMesa.so.8.0.0', 'mesa/lib/libOSMesa.so.8')
create_symlink('libOSMesa.so.8.0.0', 'mesa/lib/libOSMesa.so')
