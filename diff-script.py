#!/usr/bin/python3
import difflib
import filecmp
import time
import os

from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import shutil
import csv
from jinja2 import Environment, FileSystemLoader


# global variables
start = time.time()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

magento_diff = os.path.join(BASE_DIR, "magento_diff")
prestashop_diff = os.path.join(BASE_DIR, "prestashop_diff")

diff_lines = []

""" making sure that directories are cleared to reduce time in overwriting """

if os.path.exists(magento_diff) and os.path.isdir(magento_diff):
    if not os.listdir(magento_diff):
        shutil.rmtree(magento_diff)

if os.path.exists(prestashop_diff) and os.path.isdir(prestashop_diff):
    if not os.listdir(prestashop_diff):
        shutil.rmtree(prestashop_diff)

""" creating new directory if it does not exists """
if not os.path.exists(magento_diff):
    os.makedirs(magento_diff)

if not os.path.exists(prestashop_diff):
    os.makedirs(prestashop_diff)

# to be imported from config.py
from . import config
filecmp._filter = config._filter


# function generator the gives files in a directory
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


# download applications to compare and save to local disk
def download(version_list, whichapp):
    """
    version_list: list of versionn to download
    whichapp: application type to download
    Ask user to insert versions needs to compare against,
    download and save the files to local dir
     """
    print("Application is being downloaded.....\n")
    if whichapp == "magento":
        for version in version_list:
            zipurl = 'https://github.com/magento/magento2/archive/' + version + '.zip'
            with urlopen(zipurl) as zipresp:
                with ZipFile(BytesIO(zipresp.read())) as zfile:
                    zfile.extractall()

    elif whichapp == "prestashop":
        for version in version_list:
            zipurl = 'https://github.com/PrestaShop/PrestaShop/archive/' + version + '.zip'
            with urlopen(zipurl) as zipresp:
                with ZipFile(BytesIO(zipresp.read())) as zfile:
                    zfile.extractall()


# function to get the two dirs to compare
def get_dir(a_dir):
    """
    a_adir: directory to be search in
    returns list of subdirectories in a a directory
     """
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
            
            
# function to compare the files content in the two directories and print in to a table
def getFiles(dcmp, ignorefiles, which_app):
    left_files = ''
    """
    dcmp: dircmp object to for directory comparison
    ignorefiles: names to be ignored during comparisons
    whichapp -- application to get files
    Takes two directories and type of application,
     gives diff of two files in the two directories
     in an html format so that it can be accessed from the browser
     """
    if which_app == "magento":

        for name in dcmp.diff_files:
            if "Test" not in name:
                print(
                    "************************************************************************************************** "
                    "**************************")

                left_files = dcmp.left + '/' + name
                right_files = dcmp.right + '/' + name
                file_line_left = open(left_files, errors='ignore')
                file_line_right = open(right_files, errors='ignore')
                
                # writing into html file
                difference = difflib.HtmlDiff().make_file(file_line_left, file_line_right, left_files, right_files)
                difference_report = open(magento_diff + '/' + 'magento_diff_' + name + '.html', 'w+', encoding='utf8',
                                         errors='ignore')
                difference_report.write(difference)
                difference_report.close()
        for sub_dcmp in dcmp.subdirs.values():
            getFiles(sub_dcmp, ignorefiles, which_app)
    
    elif which_app == "prestashop":
        for name in dcmp.diff_files:

            if "test" or "Test" not in name:
                print(" . . . .  .  . . . . ..  ..  .  .  .  . .  . . . . . . . . . . . .. .  .. . . . . .. . . . . ")

                left_files = dcmp.left + '/' + name
                right_files = dcmp.right + '/' + name
                file_line_left = open(left_files, errors='ignore')
                file_line_right = open(right_files, errors='ignore')

                difference = difflib.HtmlDiff().make_file(file_line_right, file_line_left, right_files, left_files)
                difference_report = open(prestashop_diff + '/' + 'prestashop_diff_report' + name + '.html', 'w+',
                                         encoding='utf8',
                                         errors='ignore')
                difference_report.write(difference)
                difference_report.close()
                
        for sub_dcmp in dcmp.subdirs.values():
            getFiles(sub_dcmp, ignorefiles, which_app)
            
            
def main():
    """ retrieving sub directories """
    sub_directories = os.path.join(BASE_DIR, 'compare_dirs')
    directory_names = get_dir(sub_directories)

    # prompt user which application to filter
    which_app = input("which application do you want to filter: \n")
    version1 = input("Enter the first version : \n")
    version2 = input("Please also enter the second version : \n")
    version_list = [version1, version2]
    if which_app.lower() == "magento":

        dir1_name = "magento2-" + version1
        dir2_name = "magento2-" + version2
        dir_to_compare = [dir1_name, dir2_name]

        directory_1, directory_2 = dir_to_compare

        # check if applications are already downloaded
        result = all(elem in directory_names for elem in dir_to_compare)

        if result:
            """function compare is called """
            print("Comparing all files in each directories ......\n")
            dcmp = filecmp.dircmp(directory_1 + '/app/code/magento', directory_2 + '/app/code/magento',
                                  ignore=ignore_files_magento)

            print("Please give me a second until i write the diff in an html file ......\n")

            getFiles(dcmp, ignore_files_magento, which_app.lower())
        else:
            """function download is called """
            download(version_list, which_app.lower())

            print("Comparing all files in each directories ......\n")

            dcmp = filecmp.dircmp(directory_1 + '/app/code/magento', directory_2 + '/app/code/magento',
                                  ignore=ignore_files_magento)

            print("Please give me a second until i write the diff in an html file ......\n")

            getFiles(dcmp, ignore_files_magento, which_app.lower())
            end = time.time()

            print("Diff processing is complete with in %s seconds" % (end - start))

    elif which_app.lower() == "prestashop":
        dir1_name = "PrestaShop-" + version1
        dir2_name = "PrestaShop-" + version2
        dir_to_compare = [dir1_name, dir2_name]
        directory_1, directory_2 = dir_to_compare
        # check if applications are already downloaded
        result = all(elem in directory_names for elem in dir_to_compare)

        if result:
            """function compare is called """

            print("Comparing all files in each directories ......\n")

            dcmp = filecmp.dircmp(directory_1, directory_2,
                                  ignore=ignore_files_prestashop)

            print("Please give me a second until i write the diff in an html file........ \n")

            getFiles(dcmp, ignore_files_prestashop, which_app.lower())
    
            end = time.time()

            print("Diff processing is complete with in %s seconds" % (end - start))
            
        else:
            """function download is called """
            download(version_list, which_app.lower())

            print("Comparing all files in each directories ......\n")

            dcmp = filecmp.dircmp(directory_1, directory_2,
                                  ignore=ignore_files_prestashop)
            print("Please give me a second until i write the diff in an html file ...... \n")

            getFiles(dcmp, ignore_files_prestashop, which_app.lower())


if __name__ == '__main__':
    main()