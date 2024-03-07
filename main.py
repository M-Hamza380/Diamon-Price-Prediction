from src.mlReg.utils.logger import logger
from src.mlReg.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlReg.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

Stage_Name = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {Stage_Name} has started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>> Stage {Stage_Name} has completed <<<<<<')
except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Data Validation Stage"

try:
    logger.info(f">>>>>> Stage {Stage_Name} has started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {Stage_Name} has completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
