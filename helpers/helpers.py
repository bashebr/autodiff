from zipfile import ZipFile
from io import BytesIO
from urllib.request import urlopen

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

