from src.mlReg.utils.logger import logger
from src.mlReg.config.configuration import ConfigurationManager
from src.mlReg.components.model_evaluation import ModelEvaluation

Stage_Name = "Model Evaluation Stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config= model_evaluation_config)
        model_evaluation.save_result()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {Stage_Name} has started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {Stage_Name} has completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e