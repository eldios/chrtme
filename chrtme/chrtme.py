#!/usr/bin/env python
# coding: utf-8

version = '0.0.4'
author = """
Emanuele 'Lele' Calo'
Email:<lele [at] quasinormale [dot] it>
Github/Twitter: eldios
"""


# parse CLI arguments
def parsecliargs():
    """parge CLI arguments"""
    import argparse,os

    # script description
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description = '''
chrtme - chroot me is a management tool for chroot enviroments.
    ''',
        allow_abbrev = False)

    # arguments
    parser.add_argument('-v','--version', action='version',
        version="%(prog)s {}\n{}".format(version,author))
    parser.add_argument('-d','--debug', action='store_true',
        help='Enable debugging info')
    parser.add_argument('-f','--force', action='store_true',
        help='Force script execution, besides warnings (eg: not running script as root)')

    parser.add_argument('-t','--tmp', action='store', default='/tmp/',
        help='Specify temp directory location to save the downloaded image. Default "/tmp/"')
    parser.add_argument('-l','--location', action='store', default='./rootfs/',
        help='Specify the target directory to extract the downloaded image. Default "./rootfs/"')
    parser.add_argument('-r','--rm', action='store_true',
        help='Remove chroot directory after executing the task')
    parser.add_argument('-k','--keeptmp', action='store_true',
        help='Keep the downloaded image temporary file after the script exits')

    parser.add_argument('image', metavar='image', nargs=1,
        help="specify the image URL or location. The image should be a .tar file, possibly compressed with gzip, bzip or xz")
    parser.add_argument('cmd', metavar='cmd', nargs='+',
        help='Specify command to be run inside the chroot. If "-" chars are present use "--" before specifying the command')

    # argparse magic
    args = parser.parse_args()

    if args.image:
        args.image = args.image[0]

    # TODO: yikes.. please rewrite this chunk of code in a more reusable way
    # normalize paths
    if (args.location):
        args.location = os.path.realpath(args.location)
    if (args.tmp):
        args.tmp = os.path.realpath(args.tmp)

    # print args for debugging purposes
    if ( args.debug ):
        print('Parsed args => {}'.format(args))

    return args


# Download images in TMP directory or specified location
def download(image,tmp_dir,debug=False):
    """Download images in TMP directory or specified location"""
    import os
    import urllib.request
    from urllib.parse import urlparse

    url = urlparse(image)
    filename = urlparse(image).path.split('/')[-1]
    if debug:
        print('Image filename parse to {}'.format(filename))

    abs_path = os.path.join(tmp_dir,filename)
    if debug:
        print('Image absolute path set to {}'.format(abs_path))

    try:
        if os.stat(abs_path):
            if debug:
                print('Image {} found locally! Skipping download.'.format(abs_path))
            return abs_path
        elif os.stat(image):
            if debug:
                print('Image {} found locally! Skipping download.'.format(image))
            return image
    except FileNotFoundError:
        if debug:
            print('Image {} or {} NOT found locally'.format(image,abs_path))

        # downloading file now
        if url.scheme:
            # this means it's a real URL
            try:
                if debug:
                    print('Downloading {} to {}'.format(image,abs_path))
                urllib.request.urlretrieve(url.geturl(),abs_path)
                return abs_path
            except:
                print('Something bad happened during the download')
                raise
        else:
            # this means it's probably a local path
            if debug:
                print('NOT Downloading: "{}" seems a local system path.'.format(abs_path))
            return abs_path


# Extract downloaded image
def extractimage(image, target_location, debug=False):
    """Extract image to specified location"""
    import os,tarfile

    try:
        if os.stat(target_location):
            if debug:
                print('chroot directory {} found locally! Skipping extraction.'.format(target_location))
            return target_location
    except FileNotFoundError:
        if debug:
            print('chroot directory {} NOT found locally'.format(target_location))

        # extracting image now
        try:
            if tarfile.is_tarfile(image):
                if debug:
                    print('Image {} is a tarfile'.format(image))
            else:
                if debug:
                    print('Image {} is NOT a tarfile'.format(image))

            with tarfile.open(image,mode='r') as f:
                if debug:
                    print('Extracting {} in {}'.format(image,target_location))
                f.extractall(target_location)
        except:
            print('Something bad happened during the extraction')
            raise

    return target_location


# Run specified command inside chroot
def runcmd(location,cmd,debug=False):
    """Run specified command inside the chroot"""
    import os
    cmd = " ".join(cmd) # convert command list to string

    # save real_root to exit chroot env
    real_root = os.open("/", os.O_RDONLY)

    if debug:
        print('Cd-ing in {}'.format(location))
    os.chdir(location)

    if debug:
        print('Chrooting in {}'.format(location))
    os.chroot(location)

    if debug:
        print('Running "{}" in {}'.format(cmd,location))
    output = os.system(cmd)

    # back to real_root to exit chroot env
    if debug:
        print('Closing chroot, back to real root')
    os.fchdir(real_root)
    os.chroot(".")
    os.close(real_root)

    # return cmd output
    return output


# clean image and other leftovers
def cleanup(location,tmp_file,rm_chroot,keep_tmp,debug):
    """clean image and temporary file leftovers"""
    import shutil,os

    # cleaning chroot directory
    if rm_chroot:
        try:
            if os.stat(location):
                if debug:
                    print('Cleaning chroot dir {}'.format(location))
                shutil.rmtree(location)
        except FileNotFoundError:
            if debug:
                print('chroot directory {} not found'.format(location))
            pass
        except:
            if debug:
                print('Issues cleaning chroot directory {}'.format(location))
            raise

    # cleaning temp file
    if not keep_tmp:
        try:
            if os.stat(tmp_file):
                if debug:
                    print('tmp_file {} found.'.format(tmp_file))
            if debug:
                print('Cleaning tmp file {}'.format(tmp_file))
            os.remove(tmp_file)
        except FileNotFoundError:
            if debug:
                print('tmp file {} not found'.format(tmp_file))
            pass
        except:
            if debug:
                print('Found issues while cleaning {}'.format(tmp_file))
            raise


# Send signal to running chroot
def sendsignal():
    pass

# main function defition, used when call from CLI
def __main__():
    """main function definition, used when call from CLI"""
    import sys,os

    # parse command line arguments
    args = parsecliargs()

    try:
        # download image in temp directory and return downloaded image location
        downloaded_image = download(args.image, args.tmp, args.debug)

        # extract downloaded image to specified location
        chroot_location = extractimage(downloaded_image, args.location, args.debug)

        # run command inside the chroot
        taskoutput = runcmd(chroot_location, args.cmd, args.debug)

    finally:
        # cleaning chroot directory and temp leftovers
        cleanup(chroot_location,downloaded_image,args.rm,args.keeptmp,args.debug)

    sys.exit(0)

# write libraries, don't write simple scripts!
if __name__ == '__main__':
    __main__()

# vim: expandtab ts=4 sw=4 nu list
