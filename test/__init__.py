# I'm following the layout suggested at https://packaging.python.org/tutorials/packaging-projects/

# Unfortunately, using a 'src' directory does not allow the unit tests to see the source code, but
# this fixes it. Should use this more often...

import os, sys
sys.path[:0] = [ os.path.abspath(
                    os.path.join( os.path.dirname('__file__'), 'src' )
                 ) ]
