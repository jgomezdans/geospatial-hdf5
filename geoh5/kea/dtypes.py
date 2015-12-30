#!/usr/bin/env python

import gdal

# kea undefined is 0; not sure what the mapping to numpy is
NUMPY2KEADTYPE = {'int8': 1,
                  'int16': 2,
                  'int32': 3,
                  'int64': 4,
                  'uint8': 5,
                  'uin16': 6,
                  'uint32': 7,
                  'uint64': 8,
                  'float32': 9,
                  'float64': 10}

KEA2NUMPYDTYPE = {v: k for k, v in NUMPY2KEADTYPE.items()}

GDAL2KEADTYPE = {gdal.GDT_Unknown: 0,
                 gdal.GDT_Int16: 2,
                 gdal.GDT_Int32: 3,
                 gdal.GDT_Byte: 5,
                 gdal.GDT_UInt16: 6,
                 gdal.GDT_UInt32: 7,
                 gdal.GDT_Float32: 9,
                 gdal.GDT_Float64: 10}

KEA2GDALDTYPE = {v: k for k, v in GDAL2KEADTYPE.items()}