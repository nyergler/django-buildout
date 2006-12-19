import os
import shutil

def install_static(prefix, source_path, static_root):
    """Recursively copy the files from [source_path] to [static_root]/[prefix]).
    If the target path, [static_root]/[prefix], exists, it *will* be
    removed.

    Returns a list of files installed in the target path."""

    result = []

    # determine our target path for the static files
    target_path = os.path.join(static_root, prefix)

    # check if the target exists, and if it does, remove it
    if os.path.exists(target_path):
        shutil.rmtree(target_path)
        
    # copy the files
    shutil.copytree(source_path, target_path)

    # walk the target path to get a list of all files
    for dirname, dirpaths, filenames in os.walk(target_path):

        for fn in filenames:
            result.append(os.path.join(dirname, fn))

    # return a list of files we installed
    return result

    
