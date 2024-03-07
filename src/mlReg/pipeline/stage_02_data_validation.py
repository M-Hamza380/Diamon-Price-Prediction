from src.mlReg.utils.logger import logger
from src.mlReg.config.configuration import ConfigurationManager
from src.mlReg.components.data_validation import DataValidation


Stage_Name = 'Data Validation Stage'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config= data_validation_config)
        data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {Stage_Name} has started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {Stage_Name} has completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

