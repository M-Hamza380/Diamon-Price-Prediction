from src.mlReg.utils.logger import logger
from src.mlReg.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlReg.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlReg.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.mlReg.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.mlReg.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


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


Stage_Name = 'Data Transformation Stage'

try:
    logger.info(f">>>>>> Stage {Stage_Name} has started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> Stage {Stage_Name} has completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = 'Model Trainer Stage'

try:
    logger.info(f">>>>>> Stage {Stage_Name} has started <<<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>>> Stage {Stage_Name} has completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Model Evaluation Stage"

try:
    logger.info(f">>>>>> Stage {Stage_Name} has started <<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> Stage {Stage_Name} has completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e