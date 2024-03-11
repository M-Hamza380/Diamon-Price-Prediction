
from src.mlReg.utils.logger import logger
from src.mlReg.config.configuration import ConfigurationManager
from src.mlReg.components.model_trainer import ModelTrainer



Stage_Name = 'Model Trainer Stage'

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config= model_trainer_config)
        model_trainer.training()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>>> Stage {Stage_Name} has started <<<<<<')
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {Stage_Name} has  completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

