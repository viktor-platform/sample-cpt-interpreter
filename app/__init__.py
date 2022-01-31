"""Copyright (c) 2022 VIKTOR B.V.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

VIKTOR B.V. PROVIDES THIS SOFTWARE ON AN "AS IS" BASIS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from .cpt_file.controller import CPTFileController
from .project.controller import ProjectController
from .project_folder.controller import ProjectFolderController

# TODO remove this when we perform a migration to GeoFields
# ===== This is needed to prevent manifest errors ===== #
# pylint: disable=wrong-import-order
from viktor import ViktorController
from viktor.core import ParamsFromFile
from viktor.parametrization import Parametrization as ParametrizationBaseClass
from viktor.views import Summary


class Parametrization(ParametrizationBaseClass):
    pass


class TempController(ViktorController):
    viktor_typed_empty_fields = True
    parametrization = Parametrization
    summary = Summary()

    @ParamsFromFile(file_types=['.gif', '.png', '.jpg'])
    def process_file(self, file, **kwargs) -> dict:
        return {}


UserManualController = TempController
UserManualStepController = TempController