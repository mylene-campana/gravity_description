# Copyright (c) 2014-2015 CNRS
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

# Requires at least CMake 2.6 to configure the package.
CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

INCLUDE(cmake/base.cmake)
INCLUDE(cmake/python.cmake)

SET(PROJECT_NAME gravity_description)
SET(PROJECT_DESCRIPTION "Data specific to gravity environment for hpp-corbaserver")
SET(PROJECT_URL "")

SETUP_PROJECT()

FINDPYTHON()
ADD_REQUIRED_DEPENDENCY ("hpp-corbaserver >= 3")

SET(CATKIN_PACKAGE_SHARE_DESTINATION
  ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME})

install(FILES
  urdf/emu.urdf
  urdf/gravity_decor.urdf
  urdf/stone.urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/urdf
  )
install(FILES srdf/emu.srdf 
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/srdf
  )
#meshes
install(FILES
  meshes/Mars2.dae
  meshes/emu_full.dae
  meshes/bigStation.dae
  meshes/station.dae
  meshes/one_stone.dae
  meshes/stonetexture.jpg
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/meshes
  )
install (FILES
  src/hpp/corbaserver/emu/robot.py
  src/hpp/corbaserver/emu/__init__.py
  DESTINATION ${PYTHON_SITELIB}/hpp/corbaserver/emu)
SETUP_PROJECT_FINALIZE()
