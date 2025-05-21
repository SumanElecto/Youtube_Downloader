#!/usr/bin/python3

import datetime
import subprocess
import os
import platform

def condition_check():
    if platform.system() != "Linux":
        print("\nThis script is compatible with Linux only!\n")
        exit(1)
    elif os.geteuid() == 0:
        print("Please run as a non-root user!")
        exit(1)

def get_azcopy():
    print("This script needs the azcopy package")
    enquiry = input("Do you have azcopy downloaded and extracted? (y/n): ")
    if enquiry.lower() == 'y':
        az_copy_path = input("Enter path for azcopy: ")
        if not os.path.isdir(az_copy_path):
            print("\nPath should be an azcopy directory.")
        else:
            os.chdir(az_copy_path)
    elif enquiry.lower() == 'n':
        print("Downloading azcopy...\n")
        subprocess.run(['curl', '-o', 'azcopy.tar.gz', 'https://azcopyvnext.azureedge.net/release20230420/azcopy_linux_amd64_10.18.1.tar.gz'])
        os.system("mkdir azcopy && tar -xzvf azcopy.tar.gz --strip-components=1")
        os.chdir(os.getcwd() + "/azcopy")
    else:
        print("Wrong input, please try again!")

def run_azcopy_command(cmd):
    run = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, check=True)
    if run.returncode != 0:
        print("\nSomething went wrong!\n")
        exit(1)
    return run.stdout.decode('utf-8')

def blob_data():
    src_storage_name = input("Enter source storage account name: ")
    src_blob_url = f"https://{src_storage_name}.blob.core.windows.net"
    src_data_path = input("Enter source path: ")
    dest_storage_name = input("Enter destination storage account name: ")
    dest_blob_url = f"https://{dest_storage_name}.blob.core.windows.net"
    dest_container_name = input("Enter destination path: ")
    cmd = f"./azcopy copy {src_blob_url}/{src_data_path}{src_account_sas_key} {dest_blob_url}/{dest_container_name}{dest_account_sas_key} --recursive".split()
    run_azcopy_command(cmd)

def file_data():
    src_storage_name = input("Enter source storage account name: ")
    src_file_url = f"https://{src_storage_name}.file.core.windows.net"
    src_fileshare_name = input("Source fileshare name: ")
    dest_storage_name = input("Enter destination account name: ")
    dest_file_url = f"https://{dest_storage_name}.file.core.windows.net"
    dest_fileshare_name = input("Destination fileshare name: ")
    cmd = f"./azcopy copy '{src_file_url}/{src_fileshare_name}{src_account_sas_key}' '{dest_file_url}/{dest_fileshare_name}{dest_account_sas_key}' --recursive=true".split()
    run_azcopy_command(cmd)

def local_file_upload():
    local_file_path = input("Enter local file or folder path: ")
    remote_account_name = input("Enter account name: ")
    remote_fileshare_name = input("Enter fileshare name: ")
    dest_url = f"https://{remote_account_name}.file.core.windows.net/{remote_fileshare_name}"
    sas_key = input("Enter SAS key: ")
    cmd = f"./azcopy copy {local_file_path} {dest_url}{sas_key} --recursive=true".split()
    output = run_azcopy_command(cmd)
    print(output)
    print("\nData successfully uploaded!\n")

def main():
    options = '''
    1. Blob data transfer (storage to storage)
    2. File data transfer (storage to storage)
    3. Local File Data Transfer (Local to storage)
    4. Exit
    '''
    print(options)
    action_items = {'1': blob_data, '2': file_data, '3': local_file_upload}
    action_select = input("Choose action (1-4): ")

    while action_select not in action_items and action_select not in ['4', 'Exit', 'quit']:
        print("Wrong input, please try again!\n")
        action_select = input("Choose action (1-4): ")

    if action_select in action_items:
        action_items[action_select]()
    else:
        print("Good Bye")
        exit(1)

if __name__ == "__main__":
    condition_check()
    get_azcopy()
    main()
