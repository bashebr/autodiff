import difflib
import filecmp
from django.shortcuts import HttpResponse
import time

output = []
lines = []
# function to compare the files content in the two directories and print in to a table
def getdiff(dcmp, which_app):
    
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
            print(". . . .  .  . . . . ..  ..  .  .  .  . .  . . . . . . . . . . . .. .  .. . . . . .. . . . .")

            left_files = dcmp.left + '/' + name
            right_files = dcmp.right + '/' + name
            file_line_left = open(left_files, errors='ignore').readlines()
            
            file_line_right = open(right_files, errors='ignore').readlines()
            
            lines = difflib.unified_diff(file_line_left, file_line_right, left_files, right_files)
            yield [line for line in lines]
                
        for sub_dcmp in dcmp.subdirs.values():

            yield from getdiff(sub_dcmp, which_app)
    
    elif which_app == "prestashop":
        for name in dcmp.diff_files:
            print(" . . . .  .  . . . . ..  ..  .  .  .  . .  . . . . . . . . . . . .. .  .. . . . . .. . . . . ")

            left_files = dcmp.left + '/' + name
            right_files = dcmp.right + '/' + name
            file_line_left = open(left_files, errors='ignore').readlines()
            file_line_right = open(right_files, errors='ignore').readlines()

            lines = difflib.unified_diff(file_line_right, file_line_left, left_files, right_files, '', 3)
            yield [line for line in lines]
                        
        for sub_dcmp in dcmp.subdirs.values():

            yield from getdiff(sub_dcmp, which_app)
    elif which_app == "wordpress":
        for name in dcmp.diff_files:
            print(" . . . .  .  . . . . ..  ..  .  .  .  . .  . . . . . . . . . . . .. .  .. . . . . .. . . . . ")

            left_files = dcmp.left + '/' + name
            right_files = dcmp.right + '/' + name
            file_line_left = open(left_files, errors='ignore').readlines()
            file_line_right = open(right_files, errors='ignore').readlines()

            lines = difflib.unified_diff(file_line_right, file_line_left, left_files, right_files, '', n=3, lineterm='\n')
            yield [line for line in lines]
                        
        for sub_dcmp in dcmp.subdirs.values():

            yield from getdiff(sub_dcmp, which_app)
        
            