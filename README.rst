mp3 packer
==========

Creates lower bitrate versions of all music files in a file tree.

If you have a folder (and subfolders) full of music in a high bitrate,
you can use this program to create 128 kBit/s versions of each file. All
compressed files are cached in a hidden directory in your home
directory. You can then use a tool like ``rsync`` to move the compressed
music to your space limited mobile device.

usage
-----

Say have two tracks in your library:

::

    /home/user/Musik/Artist/Album/14 - Track.mp3
    /home/user/Musik/Artist/Album/06 - Song.mp3

Call ``mp3-packer``:

::

    mp3-packer /home/user/Musik

After you call ``mp3-packer`` you will have these files::

::

    /home/user/.cache/mp3_packer/128/home/user/Musik/Artist/Album/14 - Track.mp3
    /home/user/.cache/mp3_packer/128/home/user/Musik/Artist/Album/06 - Song.mp3

