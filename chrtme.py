#!/usr/bin/env python
# coding: utf-8

version = '0.0.1'
author = """
Emanuele 'Lele' Calo'
Email:<lele [at] quasinormale [dot] it>
Github/Twitter: eldios
"""

import datetime
from random import choice as randchoice
from random import randint

def parsecliargs():
	import argparse

	# script description
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description = '''
chrtme - chroot me is a management tool for chroot enviroments.
	''',
		allow_abbrev = False)

	# arguments
	parser.add_argument('-v','--version', action='version', version="%(prog)s {}\n{}".format(version,author))
	parser.add_argument('-d','--debug', action='store_true',
		help='Enable debugging info')
	parser.add_argument('-f','--force', action='store_true',
		help='Force script execution, besides warnings (eg: not running script as root)')

	parser.add_argument('-r','--rm', action='store_true',
		help='*TODO* Remove chroot directory after executing the task')
	parser.add_argument('-F','--format', action='store', default='tar',
		help='*TODO* Specify format for the downloded image. Can be "tar", "tgz"|"tar.gz", "tar.xz", "tar.bz2". Default "tar"')
	parser.add_argument('-t','--tmp', action='store', default='/tmp',
		help='Specify temp directory to be used during the image download. Default "/tmp"')
	parser.add_argument('-l','--location', action='store', default='./rootfs',
		help='Specify the target directory to extract the downloaded image. Default "./rootfs"')

	parser.add_argument('url', metavar='url', nargs=1,
		help='specify url for the image to be downloaded')
	parser.add_argument('cmd', metavar='cmd', nargs='+',
		help='Specify the command to run inside the chroot')

	# argparse magic
	args = parser.parse_args()

	# print args for debugging purposes
	if ( args.debug ):
		print('Parsed args => {}'.format(args))

	return args

# Download images in TMP directory
def download(url,tmp_dir='/tmp'):
	pass

# Check downloaded image
def checkimage():
	pass

# Extract downloaded image
def extractimage():
	pass

# Run specified command inside chroot
def runcmd():
	pass

# Send signal to running chroot
def sendsignal():
	pass

# main function defition, used when call from CLI
def __main__():
	"""main function defition, used when call from CLI"""

	# parse command line arguments
	args = parsecliargs()

	# download image in temp directory and return downloaded image location
	downloaded_image = download(args.url, args.tmp)

	# extract downloaded image to specified location
	chroot_location = extractimage(downloaded_image, args.location)

	# run command inside the chroot
	taskoutput = runcmd(chroot_location, args.cmd)

# write libraries, don't write simple scripts!
if __name__ == '__main__':
	__main__()

# vim: noexpandtab ts=4 sw=4 nu nolist
