gravity_description
===================
This package containts a problem for motion planning: a freeflyer robot that should move in a space-station decor.

The robot can be an external robot (e.g. HRP-2 is use in some scripts) of the emu robot: a simpler freeflyer-emu-mesh which is installed with this package.

The package contains:

  - URDF/SRDF files describing the objects,

  - Some Python scripts going along with HPP software (github.com/humanoid-path-planner) for motion planning,

The problem can be vizualised with HPP-gepetto-viewer (github.com/humanoid-path-planner) or with RViz (must create .launch files).

To install the package with cmake, simply:

  - Create a 'build' directory in the source package,

  - in the created /build, configure the package - particularly the 'install path variable' - and install it with 'ccmake ..' and 'make install'.

