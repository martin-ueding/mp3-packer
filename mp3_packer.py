#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2011 Martin Ueding <dev@martin-ueding.de>

import optparse
from gettext import gettext
import os
import sys
import shutil

tempnumber = 1

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
        if name[-4:] == ".mp3" or name[-4:] == ".m4a":
            infile = dirname+"/"+name
            outfile = destpath+dirname+"/"+name[:-4]+".mp3"
            if not os.path.exists(outfile):
                encode(bitrate, infile, outfile)
            

def clearfolder(ignores, dirname, names):
    realdir = dirname[len(destpath):]

    for name in names:
        currentfile = realdir+"/"+name
        cachefile = dirname+"/"+name
        # XXX make this check general, e.g. listing dir contents and checking names
        if not (os.path.exists(currentfile) or os.path.exists(currentfile[:-4]+".m4a")):
            print "missing: %s" % currentfile
            if os.path.isdir(cachefile):
                shutil.rmtree(cachefile)
            else:
                os.remove(cachefile)


def encode(bitrate, infile, outfile):
    # create the dir so that lame does not complain
    dir_of_infile = os.path.dirname(outfile)
    if not os.path.exists(dir_of_infile):
        os.makedirs(dir_of_infile)

    global tempnumber
    tempfile = "mp3_packer-temp-%d.mp3" % tempnumber
    tempnumber += 1

    # encode the file
    print gettext("encoding %s") % infile
    if engine == "lame":
        command = 'lame --quiet -b %d "%s" "%s"' % (bitrate, infile, tempfile)
    if engine == "ffmpeg":
        command = 'ffmpeg -i "%s" -map_meta_data "%s":"%s" -acodec libmp3lame -ac 2 -ab %dk "%s"' % (infile, infile, tempfile, bitrate, tempfile)

    command = command + ' && mv "%s" "%s"' % (tempfile, outfile)

    os.system(command)

    # delete the tempfile in case anything went wrong
    if os.path.exists(tempfile):
        os.remove(tempfile)


if __name__ == "__main__":
    main()

