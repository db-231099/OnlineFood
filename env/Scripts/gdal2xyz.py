#!D:\MCA final year project docs\mca-final-year-project\env\Scripts\python.exe

import sys

from osgeo.gdal import UseExceptions, deprecation_warn

# import osgeo_utils.gdal2xyz as a convenience to use as a script
from osgeo_utils.gdal2xyz import *  # noqa
from osgeo_utils.gdal2xyz import main

UseExceptions()

deprecation_warn("gdal2xyz")
sys.exit(main(sys.argv))
