#!/usr/bin/env python
# Copyright (c) 2014 CNRS
# Author: Mylene Campana
#
# This file is part of gravity_description.
# gravity_description is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# gravity_description is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# gravity_description.  If not, see
# <http://www.gnu.org/licenses/>.

from hpp.corbaserver.robot import Robot as Parent

##
#  Control of emu robot in hpp
#
#  This class implements a client to the corba server implemented in
#  hpp-corbaserver. It derive from class hpp.corbaserver.robot.Robot.

class Robot (Parent):
    ##
    #  Information to retrieve urdf and srdf files.
    packageName = "gravity_description"
    ##
    #  Information to retrieve urdf and srdf files.
    urdfName = "emu"
    urdfSuffix = ""
    srdfSuffix = ""

    def __init__ (self, robotName, load = True):
        Parent.__init__ (self, robotName, "freeflyer", load)
        self.tf_root = "emu_base"
