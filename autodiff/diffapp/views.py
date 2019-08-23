from django.shortcuts import render
import filecmp, difflib
import os
# import time

from .helpers import download
from .compare import getdiff
from .forms import GetVersionForm
from .config import (
    directory_names, IGNORE_FILES_MAGENTO,
    IGNORE_FILES_PRESTASHOP, _filter
)

# to be imported from config.py
filecmp._filter = _filter

def get_version(request):
    # start = time.time()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GetVersionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return display(request)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GetVersionForm()

    return render(request, 'diffapp/diffapp.html', {'form': form})

def display(request):
    output = []
    # process version entered by user
    version_1 = request.POST['version_1']
    version_2 = request.POST['version_2']
    which_app = request.POST['which_app']


    # compare dirs
    version_list = [version_1, version_2]
    if which_app.lower() == "magento":

        dir1_name = "magento2-" + version_1
        dir2_name = "magento2-" + version_2
        dir_to_compare = [dir1_name, dir2_name]

        # directory_1, directory_2 = dir_to_compare

        # check if applications are already downloaded
        result = all(elem in directory_names for elem in dir_to_compare)

        if result:
            """function compare is called """
            print("Comparing all files in each directories ......\n")
            dcmp = filecmp.dircmp(dir1_name + '/app/code/magento', dir2_name + '/app/code/magento',
                                  ignore=IGNORE_FILES_MAGENTO)

            print("Please give me a second until i write the diff in an html file ......\n")

            output = getdiff(dcmp, which_app.lower())
        else:
            """function download is called """
            download(version_list, which_app.lower())

            print("Comparing all files in each directories ......\n")

            dcmp = filecmp.dircmp(dir1_name + '/app/code/magento', dir2_name + '/app/code/magento',
                                  ignore=IGNORE_FILES_MAGENTO)

            print("Please give me a second until i write the diff in an html file ......\n")

            output = getdiff(dcmp, which_app.lower())
            # end = time.time()

            # print("Diff processing is complete with in %s seconds" % (end - start))

    elif which_app.lower() == "prestashop":
        dir1_name = "PrestaShop-" + version_1
        dir2_name = "PrestaShop-" + version_2
        dir_to_compare = [dir1_name, dir2_name]
        # directory_1, directory_2 = dir_to_compare
        # check if applications are already downloaded
        result = all(elem in directory_names for elem in dir_to_compare)

        if result:
            """function compare is called """

            print("Comparing all files in each directories ......\n")

            dcmp = filecmp.dircmp(dir1_name, dir2_name,
                                    ignore=IGNORE_FILES_PRESTASHOP)

            print("Please give me a second until i write the diff in an html file........ \n")

            output = getdiff(dcmp, which_app.lower())
            
        else:
            """function download is called """
            download(version_list, which_app.lower())

            print("Comparing all files in each directories ......\n")

            dcmp = filecmp.dircmp(dir1_name, dir2_name,
                                    ignore=IGNORE_FILES_PRESTASHOP)
            
            print("Please give me a second until i write the diff in an html file ...... \n")
            
            output = getdiff(dcmp, which_app.lower())
    elif which_app.lower() == "wordpress":
        dir1_name = "wordpress-" + version_1
        dir2_name = "wordpress-" + version_2
        dir_to_compare = [dir1_name, dir2_name]
        # directory_1, directory_2 = dir_to_compare
        # check if applications are already downloaded
        result = all(elem in directory_names for elem in dir_to_compare)

        if result:
            """function compare is called """

            print("Comparing all files in each directories ......\n")
            directory1 = os.path.dirname(dir1_name + '/wordpress')
            directory2 = os.path.dirname(dir2_name + '/wordpress')
            dcmp = filecmp.dircmp(directory1, directory2,
                                    ignore=IGNORE_FILES_PRESTASHOP)

            print("Please give me a second until i write the diff in an html file........ \n")

            output = getdiff(dcmp, which_app.lower())
            
        else:
            """function download is called """
            download(version_list, which_app.lower())

            print("Comparing all files in each directories ......\n")
            directory1 = os.path.dirname(dir1_name + '/wordpress')
            directory2 = os.path.dirname(dir2_name + '/wordpress')
            dcmp = filecmp.dircmp(directory1, directory2,
                                    ignore=IGNORE_FILES_PRESTASHOP)
            
            print("Please give me a second until i write the diff in an html file ...... \n")
            
            output = getdiff(dcmp, which_app.lower())

    return render(request, 'diffapp/display.html', {'files': output, 'which_app': which_app, 'version_1': version_1, 'version_2': version_2})

