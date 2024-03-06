import os
import zipfile
import gdown
from pathlib import Path

from src.mlReg.entity.config_entity import DataIngestionConfig
from src.mlReg.utils.logger import logger
from src.mlReg.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                dataset_url = self.config.source_URL
                zip_download_dir = self.config.local_data_file
                logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

                file_id = dataset_url.split("/")[-2]
                prefix = "https://drive.google.com/uc?/export=download&id="
                url = prefix+file_id
                gdown.download(url, zip_download_dir)
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
        except Exception as e:
            logger.info(e)
            raise e
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)


