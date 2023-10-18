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


def generate_env_file_for_cloud_storage (configure_aws = False, configure_azure = False ):
    file = open(".env", "w")
    if configure_aws:
        file.write("AWS_ACCESS_KEY_ID =\n")
        file.write("AWS_SECRET_ACCESS_KEY =\n")
        file.write("AWS_BUCKET_NAME =\n")
        file.write("\n")
    if configure_azure:
        file.write("AZURE_ACCOUNT_NAME =\n")
        file.write("AZURE_BLOB_CONTAINER_NAME =\n")
        file.write("AZURE_SAS_CREDENTIAL =\n")
    file.close()


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

        # # remove not used cloud storage client(s)
        # if '{{cookiecutter.cloud_storage}}' == 'aws':
        #     remove_file(os.path.join('src', 'cloud_storage', 'cloud_storage_azure.py'))
        #     generate_env_file_for_cloud_storage(configure_aws=True, configure_azure=False)
        # elif '{{cookiecutter.cloud_storage}}' == 'azure':
        #     remove_file(os.path.join('src', 'cloud_storage', 'cloud_storage_aws.py'))
        #     generate_env_file_for_cloud_storage(configure_aws=False, configure_azure=True)
        # elif '{{cookiecutter.cloud_storage}}' == 'both':
        #     generate_env_file_for_cloud_storage(configure_aws=True, configure_azure=True)
        # else:
        #     remove_dir(os.path.join('src', 'cloud_storage'))
        #     if os.path.exists('.env'):
        #         remove_file('.env')

        cloud_storage_selection = '{{cookiecutter.cloud_storage}}'
        cloud_storage_path = 'src/cloud_storage'

        aws_file_path = os.path.join(cloud_storage_path, 'cloud_storage_aws.py')
        azure_file_path = os.path.join(cloud_storage_path, 'cloud_storage_azure.py')

        if cloud_storage_selection == 'aws':
            create_if_not_exists(aws_file_path, is_file=True)
            remove_file(azure_file_path)
            generate_env_file_for_cloud_storage(configure_aws=True, configure_azure=False)

        elif cloud_storage_selection == 'azure':
            create_if_not_exists(azure_file_path, is_file=True)
            remove_file(aws_file_path)
            generate_env_file_for_cloud_storage(configure_aws=False, configure_azure=True)

        elif cloud_storage_selection == 'both':
            create_if_not_exists(aws_file_path, is_file=True)
            create_if_not_exists(azure_file_path, is_file=True)
            generate_env_file_for_cloud_storage(configure_aws=True, configure_azure=True)

        else:
            remove_file(aws_file_path)
            remove_file(azure_file_path)
            remove_dir(cloud_storage_path)
            if os.path.exists('.env'):
                remove_file('.env')

    except Exception as e:
        print(e)



