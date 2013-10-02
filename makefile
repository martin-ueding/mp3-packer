# Copyright © 2012-2013 Martin Ueding <dev@martin-ueding.de>

###############################################################################
#                                   License                                   #
###############################################################################
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

pythonfiles:=$(wildcard *.py)

mp3-packer.1: mp3-packer.1.rst
	rst2man $< $@

html: html/index.html

html/index.html: mp3-packer $(pythonfiles)
	epydoc -v $^

.PHONY: clean
clean:
	$(RM) *.pyc
	$(RM) -r html
	$(RM) mp3-packer.1
	$(RM) mp3-packer.1.gz
	$(RM) mp3-packerc

install:
	mkdir -p $(DESTDIR)/usr/share/man/man1/
	gzip -c mp3-packer.1 > $(DESTDIR)/usr/share/man/man1/mp3-packer.1.gz
	mkdir -p $(DESTDIR)/usr/bin/
	install mp3-packer $(DESTDIR)/usr/bin/
