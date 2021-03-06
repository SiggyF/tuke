# vim: tabstop=4 expandtab shiftwidth=4 fileencoding=utf8
# ### BOILERPLATE ###
# Tuke - Electrical Design Automation toolset
# Copyright (C) 2008 Peter Todd <pete@petertodd.org>
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ### BOILERPLATE ###

from Tuke import Element,Id

from Tuke.sch import Component,Pin
from Tuke.pcb import Footprint

class Symbol(Component):
    """Defines a Symbol.
   
    A Symbol is a Component with a Footprint.
    """

    def create_linked_pins(self,pins):
        """Create pins and link them to the footprint.

        Pins created are linked to sequential footprint id numbers, starting
        from 1.

        """

        for i,p in enumerate(pins):
            if not isinstance(p,Pin):
                p = Pin(id=p)
            self.add(p)
            p.connects.add(Id('footprint/_%d' % (i + 1)))
