from pathlib import Path

from src.mlReg.components.data_transformation import DataTransformation
from src.mlReg.config.configuration import ConfigurationManager
from src.mlReg.utils.logger import logger

Stage_Name = 'Data Transformation Stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
            status = f.read().split(" ")[-1]
        
        if status == 'True':
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config= data_transformation_config)
            data_transformation.spliting_data()
        else:
            raise Exception("Your data schema is not valid")


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {Stage_Name} has started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {Stage_Name} has completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e


