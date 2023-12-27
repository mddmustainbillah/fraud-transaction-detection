# import os
# import requests
# import zipfile
# from mlProject import logger
# from src.mlProject.utils.common import get_size
# from src.mlProject.entity.config_entity import DataIngestionConfig
# from pathlib import Path

# class DataIngestion:
#     def __init__(self, config: DataIngestionConfig):
#         self.config = config
    
    # def download_file(self):
    #     if not os.path.exists(self.config.local_data_file):
    #         # Make a HEAD request to get the file size without downloading the entire file
    #         response = requests.head(self.config.source_URL)

    #         # Check if the request was successful (status code 200) and if the 'Content-Length' header is present
    #         if response.status_code == 200 and 'Content-Length' in response.headers:
    #             file_size = int(response.headers['Content-Length'])
    #             logger.info(f"File size: {file_size} bytes")

    #             # Download the file if it doesn't exist
    #             filename, headers = request.urlretrieve(
    #                 url=self.config.source_URL,
    #                 filename=self.config.local_data_file
    #             )
    #             logger.info(f"{filename} downloaded! with the following info:\n{headers}")
    #         else:
    #             logger.error("Failed to retrieve file size. Check the URL and try again.")
    #     else:
    #         logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    # def extract_zip_file(self):
    #     unzip_path = self.config.unzip_dir
    #     os.makedirs(unzip_path, exist_ok=True)
    #     with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
    #         zip_ref.extractall(unzip_path)




import os
import urllib.request as request
import zipfile
from mlProject import logger
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataIngestionConfig
from pathlib import Path
import kaggle


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
