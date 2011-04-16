#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2011 Martin Ueding <dev@martin-ueding.de>

import optparse
from gettext import gettext
import os
import sys

def main():
	parser = optparse.OptionParser(usage=gettext("%prog path"), description=gettext("Traverses through a folder and creates a copy of the folder structure but compresses everything to a certain bitrate."))
	parser.add_option("--bitrate", dest="bitrate", type="int", default=128, help=gettext("bitrate in kbit [default: %default]"))
	parser.add_option("--engine", dest="engine", default="ffmpeg", help=gettext("engine to use (ffmpeg or lame) [default: %default]"))

	(options, args) = parser.parse_args()

	global engine
	engine = options.engine

	if len(args) != 1:
		print gettext("call with -h to get help")
		sys.exit(1)

	srcpath = os.path.abspath(args[0])
	global destpath
	destpath = os.path.expanduser("~/.mp3_packer/"+str(options.bitrate))

	print gettext("reading from %s") % srcpath
	print gettext("writing to %s") % destpath
	print

	# encode the all new files
	os.path.walk(srcpath, parsefolder, options.bitrate)

	# delete files that are no longer needed
	os.path.walk(destpath, clearfolder, None)

	# TODO delete empty directories


def parsefolder(bitrate, dirname, names):
	for name in names:
		# TODO add support for AAC too
		if name[-4:] == ".mp3" or name[-4:] == ".m4a":
			infile = dirname+"/"+name
			outfile = destpath+dirname+"/"+name
			if not os.path.exists(outfile):
				encode(bitrate, infile, outfile)
			

def clearfolder(ignores, dirname, names):
	realdir = dirname[len(destpath):]

	for name in names:
		currentfile = realdir+"/"+name
		if not os.path.exists(currentfile):
			print "missing: %s" % currentfile
			os.remove(dirname+"/"+name)


def encode(bitrate, infile, outfile):
	# create the dir so that lame does not complain
	# TODO use os.path here
	os.system("mkdir -p '%s'" % os.path.dirname(outfile))

	# encode the file
	print gettext("encoding %s") % infile
	if engine == "lame":
		command = 'lame --quiet -b %d "%s" "%s"' % (bitrate, infile, outfile)
	if engine == "ffmpeg":
		command = 'ffmpeg -i "%s" -acodec libmp3lame -ac 2 -ab %dk "%s"' % (infile, bitrate, outfile)

	os.system(command)


if __name__ == "__main__":
	main()

