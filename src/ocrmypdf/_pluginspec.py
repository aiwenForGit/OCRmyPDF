# © 2020 James R. Barlow: github.com/jbarlow83
#
# This file is part of OCRmyPDF.
#
# OCRmyPDF is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OCRmyPDF is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OCRmyPDF.  If not, see <http://www.gnu.org/licenses/>.

from argparse import Namespace

import pluggy
from PIL import Image

from ocrmypdf.pdfinfo import PdfInfo

hookspec = pluggy.HookspecMarker('ocrmypdf')

# pylint: disable=unused-argument


@hookspec
def prepare(options: Namespace) -> None:
    """Called to notify a plugin that a file will be processed.

	The plugin may modify the options. All objects that are in options must
	be picklable so they can be marshalled to child worker processes.

    Typically, a plugin will call ``registry.register_plugin(__name__)`` to register
    all of its public functions with the plugin registry. Functions that are
    not intended for registration should be prefixed with an underscore.
    Functions that imported from other modules will be ignored by
    ``.register_plugin()``. For example if you use ``from os import basename``,
    ``basename`` will not be registered.
	"""


@hookspec
def validate(pdfinfo: PdfInfo, options: Namespace) -> None:
    """Called to give a plugin an opportunity to review options and pdfinfo.

    options contains the "work order" to process a particular file. pdfinfo
    contains information about the input file obtained after loading and
    parsing.

    The plugin may raise InputFileError or any ExitCodeException to request
    normal termination. If the plugin raises another exception type, ocrmypdf
    will abort with an error and hold the plugin responsible.
    """


@hookspec
def filter_ocr_image(image: Image) -> Image:
    """Called to filter the image before it is sent to OCR.

    This is the image that OCR sees, not what the user sees when they view the
    PDF.
    """