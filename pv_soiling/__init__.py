from .pv_soiling import pm_frame
from .pv_soiling import result_frame
from .pv_soiling import create_pm_frame

__author__ = "Michael Deceglie"
__email__ = "michael.deceglie@nrel.gov"
__status__ = "Beta"

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def setup_logging(default_path='logging.json',
                  default_level=logging.INFO,
                  env_key='LOG_CFG'):
    """Setup logging configuration """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    # return logger,log_file_handler


setup_logging()


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

