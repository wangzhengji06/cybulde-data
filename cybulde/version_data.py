from pathlib import Path

from cybulde.config_schemas.config_schema import Config
from cybulde.utils.config_utils import get_config
from cybulde.utils.data_utils import initialized_dvc


@get_config(config_path="../configs", config_name="config")
def entrypoint(config: Config) -> None:
    logger = get_logger(PATH(__file__).name)
    logger.info
    
    initialized_dvc()

if __name__ == "__main__":
    version_data()
