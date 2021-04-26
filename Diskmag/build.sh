#!/bin/bash
echo ""
echo "-------------------------------------------"
echo "Building Nomad Diskmag..."
echo ""
PYTHONOPTIMIZE=1 pyinstaller \
--clean \
--noconfirm \
--onefile \
--noconsole \
--name Nomad_Diskmag_0_WIP \
--add-data "assets/:assets/" \
--add-data "chapters/:chapters/" \
main.py
echo ""
echo "-------------------------------------------"
echo "Run ./dist/Nomad_Diskmag_0_WIP "
echo ""
echo ""