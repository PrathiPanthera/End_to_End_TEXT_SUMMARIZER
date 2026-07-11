from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.model_trainer import ModelTrainer
from text_summarizer.logging import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=trainer_config)
        model_trainer.train()