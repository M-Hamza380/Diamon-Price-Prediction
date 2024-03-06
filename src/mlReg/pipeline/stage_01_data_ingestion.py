from src.mlReg.config.configuration import ConfigurationManager
from src.mlReg.components.data_ingestion import DataIngestion
from src.mlReg.utils.logger import logger

Stage_Name = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config= data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {Stage_Name} has started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>> Stage {Stage_Name} has completed <<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e


