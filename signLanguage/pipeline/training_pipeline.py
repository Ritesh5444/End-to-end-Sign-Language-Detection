import os,sys
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.components.data_ingestion import DataIngestionConfig
from signLanguage.components.data_ingestion import DataIngestionArtifact


class TraningPipeline:

    def __init__(self):
        self.data_ingestion_config =DataIngestionConfig()


    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Entered the start ingestion method of Traning Pipeline class")
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config= self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.intiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info("Exited the start_data_ingestion_method of TraningPipeline class") 

            return DataIngestionArtifact           
        except Exception as e:
            raise SignException(e,sys)
        
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise SignException(e,sys)
