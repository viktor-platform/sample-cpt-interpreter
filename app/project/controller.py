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

from munch import Munch

from viktor.api_v1 import API
from viktor.api_v1 import EntityList
from viktor.core import ViktorController
from viktor.views import MapResult
from viktor.views import MapView
from viktor.views import Summary
from .parametrization import SampleParametrization
from ..cpt_file.constants import CPT_LEGEND
from ..cpt_file.model import CPT
from ..cpt_file.model import color_coded_cpt_map_points


class ProjectController(ViktorController):
    """Controller class which acts as interface for the Sample entity type."""
    label = "Sample"
    children = ['CPTFile']
    show_children_as = 'Table'
    parametrization = SampleParametrization
    viktor_convert_entity_field = True
    summary = Summary()

    @MapView('Map', duration_guess=2)
    def visualize_map(self, params: Munch, entity_id: int, **kwargs) -> MapResult:
        """Visualize the MapView with all CPT locations and a polyline"""

        all_cpt_files = self._get_cpt_models(entity_id)
        cpt_features = color_coded_cpt_map_points(all_cpt_files)

        return MapResult([*cpt_features], [], CPT_LEGEND)

    def _get_cpt_models(self, entity_id):
        """Obtains all child 'CPT File' entities"""
        cpt_file_entities = self._get_cpt_file_entities(entity_id, include_params=True)
        all_cpt_files = [CPT(cpt_params=cpt_entity.last_saved_params) for cpt_entity in cpt_file_entities]
        return all_cpt_files

    @staticmethod
    def _get_cpt_file_entities(entity_id: int, include_params: bool = True) -> EntityList:
        """Obtains all CPT File entities and returns them"""
        return API().get_entity(entity_id).children(entity_type_names=['CPTFile'], include_params=include_params)