from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingpipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>>>  {STAGE_NAME} Started <<<<<<<<<")
    data_ingestion_pipeline_obj = DataIngestionTrainingPipeline()
    data_ingestion_pipeline_obj.main()
    logger.info(f">>>>>>>>>  {STAGE_NAME} Completed <<<<<<")
    logger.info("#"*60 + "\n")
   

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>>>>>  {STAGE_NAME} Started <<<<<<<<<")
    data_validation_pipeline_obj = DataValidationTrainingpipeline()
    data_validation_pipeline_obj.main()
    logger.info(f">>>>>>>>>  {STAGE_NAME} Completed <<<<<<")
    logger.info("#"*60 + "\n")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>>>>>  {STAGE_NAME} Started <<<<<<<<<")
    data_transformation_pipeline_obj = DataTransformationTrainingPipeline()
    data_transformation_pipeline_obj.main()
    logger.info(f">>>>>>>>>  {STAGE_NAME} Completed <<<<<<")
    logger.info("#"*60 + "\n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training stage"

try:
    logger.info(f">>>>>>>>>  {STAGE_NAME} Started <<<<<<<<<")
    model_training_pipeline_obj = ModelTrainingPipeline()
    model_training_pipeline_obj.main()
    logger.info(f">>>>>>>>>  {STAGE_NAME} Completed <<<<<<")
    logger.info("#"*60 + "\n")

except Exception as e:
    logger.exception(e)
    raise e