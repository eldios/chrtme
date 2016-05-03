#!/usr/bin/env python
# coding: utf-8

version = '0.0.2'
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

    parser.add_argument('-t','--tmp', action='store', default='/tmp/rootfs.tmp',
        help='Specify temp file location to save the downloaded image. Default "/tmp/rootfs.tmp"')
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

    # normalize path
    if (args.location):
        args.location = os.path.realpath(args.location)

    # print args for debugging purposes
    if ( args.debug ):
        print('Parsed args => {}'.format(args))

    return args


# Download images in TMP directory or specified location
def download(image,tmp_file,debug=False):
    import os,urllib
    """Download images in TMP directory or specified location"""
    try:
        if os.stat(image):
            if debug:
                print('Image {} found locally! Skipping download.'.format(image))
    except FileNotFoundError:
        if debug:
            print('Image {} NOT found!'.format(image))

        try:
            urllib.urlretrieve(image, tmp_file)
        except:
            print('Something bad happened during the download')

    return image


# Extract downloaded image
def extractimage(image, target_location, debug=False):
    """Extract image to specified location"""
    import tarfile

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
        if debug:
            print('Cleaning chroot dir {}'.format(location))
        shutil.rmtree(location)

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
                print('tmp_file {} NOT found!'.format(tmp_file))


# Send signal to running chroot
def sendsignal():
    pass

# main function defition, used when call from CLI
def __main__():
    """main function defition, used when call from CLI"""
    import sys

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
        cleanup(args.location,args.tmp,args.rm,args.keeptmp,args.debug)

    sys.exit(0)

# write libraries, don't write simple scripts!
if __name__ == '__main__':
    __main__()

# vim: expandtab ts=4 sw=4 nu list
