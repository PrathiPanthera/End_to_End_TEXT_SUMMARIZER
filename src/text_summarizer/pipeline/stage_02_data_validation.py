from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.data_validation import DataValidation
from text_summarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=validation_config)
        validation_status = data_validation.validate_all_files_exist()
        print("Validation Status:", validation_status)