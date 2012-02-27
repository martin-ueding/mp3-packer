# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

pythonfiles:=$(wildcard *.py)

mp3-packer.1: mp3-packer.1.rst
	rst2man $< $@

doc: html/index.html

html/index.html: mp3-packer $(pythonfiles)
	epydoc -v $^

.PHONY: clean
clean:
	$(RM) *.pyc
	$(RM) -r html
	$(RM) mp3-packerc

install:
	gzip -c mp3-packer.1 $(DESTDIR)/usr/share/man/man1/mp3-packer.1.gz
