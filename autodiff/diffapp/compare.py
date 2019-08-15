import difflib
import filecmp


# function to compare the files content in the two directories and print in to a table
def getdiff(dcmp, which_app):
    tabel = []
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
                difference = difflib.HtmlDiff().make_table(file_line_left, file_line_right, left_files, right_files)
                tabel.append(difference)
                # difference_report = open(magento_diff + '/' + 'magento_diff_' + name + '.html', 'w+', encoding='utf8',
                #                          errors='ignore')
                # difference_report.write(difference)
                # difference_report.close()

        for sub_dcmp in dcmp.subdirs.values():
            getdiff(sub_dcmp, which_app)

        if not dcmp.subdirs.values():
            return tabel
    
    elif which_app == "prestashop":
        for name in dcmp.diff_files:

            if "test" or "Test" not in name:
                print(" . . . .  .  . . . . ..  ..  .  .  .  . .  . . . . . . . . . . . .. .  .. . . . . .. . . . . ")

                left_files = dcmp.left + '/' + name
                right_files = dcmp.right + '/' + name
                file_line_left = open(left_files, errors='ignore')
                file_line_right = open(right_files, errors='ignore')

                difference = difflib.HtmlDiff().make_table(file_line_right, file_line_left, right_files, left_files)
                tabel.append(difference)
                # difference_report = open(prestashop_diff + '/' + 'prestashop_diff_report' + name + '.html', 'w+',
                #                          encoding='utf8',
                #                          errors='ignore')
                # difference_report.write(difference)
                # difference_report.close()
                
        for sub_dcmp in dcmp.subdirs.values():
            getdiff(sub_dcmp, which_app)

        if not dcmp.subdirs.values():
            return tabel
