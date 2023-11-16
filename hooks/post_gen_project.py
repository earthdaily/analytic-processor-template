#!/usr/bin/env python
import os
import subprocess
import sys
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# def remove_file(filepath):
#     try:
#         os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
#     except FileNotFoundError:
#         pass
#
#
# def remove_dir(dirpath):
#     try:
#         shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))
#     except FileNotFoundError:
#         pass

def remove_file(filepath):
    full_path = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.exists(full_path):
        os.remove(full_path)

def remove_dir(dirpath):
    full_path = os.path.join(PROJECT_DIRECTORY, dirpath)
    if os.path.exists(full_path):
        shutil.rmtree(full_path)


def execute(*args, supress_exception=False, cwd=None):
    cur_dir = os.getcwd()

    try:
        if cwd:
            os.chdir(cwd)

        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        out, err = proc.communicate()
        out = out.decode('utf-8')
        err = err.decode('utf-8')
        if err and not supress_exception:
            raise Exception(err)
        else:
            return out
    finally:
        os.chdir(cur_dir)




def init_git():
    # workaround for issue #1
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        execute("git", "config", "--global", "init.defaultBranch", "main", cwd=PROJECT_DIRECTORY)
        execute("git", "init", cwd=PROJECT_DIRECTORY)

def create_if_not_exists(path, is_file=False):

    full_path = os.path.join(PROJECT_DIRECTORY, path)

    if not os.path.exists(full_path):
        if is_file:
            # Create the file along with any necessary directories.
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as file:
                pass  # Just create an empty file.
        else:
            # Create the directory.
            os.makedirs(full_path, exist_ok=True)


if __name__ == '__main__':

    try:
        init_git()
        # remove not used cloud storage client(s)
        if '{{cookiecutter.mode}}' == 'basic':
            remove_dir(os.path.join('src', 'models'))
            remove_file(os.path.join('src', 'data', '__init__.py'))
            remove_file(os.path.join('src', 'data', 'dataset.py'))


    except Exception as e:
        print(e)



