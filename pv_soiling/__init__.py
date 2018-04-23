from .pv_soiling import pm_frame
from .pv_soiling import result_frame
from .pv_soiling import create_pm_frame

__author__ = "Michael Deceglie"
__email__ = "michael.deceglie@nrel.gov"
__status__ = "Beta"

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
