.. Copyright © 2012-2014, 2016-2017 Martin Ueding <dev@martin-ueding.de>

mp3-packer
==========

I have more music than would fit onto the memory card of my phone. This is
largely due to the 256 kBit/s versions that are sold now. On the phone, I do
not really hear the difference between 256 kBit/s and 128 kBit/s, but I can
clearly see the difference in size.

This script creates a whole copy of your music library, just with a smaller
bitrate. It uses either *ffmpeg* or *lame* to convert the tracks.

Installation
------------

Just use::

    make
    sudo make install


Usage
-----

``mp3-packer path-to-music``

For more information, see ``mp3-packer -h`` or the manpage_

.. _manpage: mp3-packer.rst
