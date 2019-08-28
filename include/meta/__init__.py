"""
    fb2ics - Facebook Birthday Events to ICS (calendar) file converter.
    Copyright 2019 Hardeep Singh Narang (@hardeepnarang10)

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify,
    merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
    BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from include.meta._version import __version_info__, __version__

__author__ = 'Hardeep Singh Narang @hardeepnarang10'
__copyright__ = 'Copyright 2019'
__email__ = 'hardeepnarang10@gmail.com'
__license__ = "MIT"
__maintainer__ = 'Hardeep Singh Narang @hardeepnarang10'
__status__ = "Production"

# Make metadata public to script
__all__ = ['__author__', '__copyright__', '__email__', '__license__', '__maintainer__', '__status__', '__version_info__', '__version__']