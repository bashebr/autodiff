from fnmatch import fnmatch

# some configuration and constant variables

""" Files or directories to be ignored from the diff """
IGNORE_FILES_MAGENTO = \
    ['dev', 'test', '*.txt', 'composer.json', '*-composer-*',
     '.htaccess', 'css', 'images', 'upload.php', '*.md',
     'css', '*.yml', '*.yaml', '*.sample', '*.lock',
     '*.gitignore', '*.gitattributes', '*.dist', '*.ini',
     '*.conf', 'magento2-functional-testing-framework', 'language-*',
     'zendframework1', 'images', '*.jpeg', '*.gif', '*.png', 'inventory-composer-installer',
     'framework-amqp', '.github']

IGNORE_FILES_PRESTASHOP = \
    ['.github', 'app', 'bin', 'cache', 'config', 'docs', 'download', 'img', 'install-dev', 'js'
        , 'localization', 'modules', 'override', 'pdf', 'src', 'tests', 'test', 'tests-legacy',
     'themes', '_core', '_libraries', '_dev', 'assets', 'plugins', 'tools', 'translations',
     'travis-scripts', 'upload', 'var', 'vendor', 'webservices', '.editorconfig', '.eslintignore',
     'eslintrc.js', '.gitignore', '.php_cs.dist', '*.yml', '*.json', '*.lock', '*.md', 'diff-hooks.php',
     'error500.html', 'images.*', '*.txt', '*.png', '*.jpg', '*.jpeg', '*.gif', '*.ico']


# function to enable filtering when ignoring the files or dirs
def _filter(flist, skip):
    """
        flist -- list of list of files to check
        skip --- string or char to skip
        This overrides the core function filter in dircmp in order to include files like *.ext
        this should be placed before we call dircmp function of the filecmp module

     """
    return [item for item in flist
            if not any(fnmatch(item, pat) for pat in skip)]