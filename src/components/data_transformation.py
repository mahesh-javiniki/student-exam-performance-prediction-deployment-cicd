import os
import sys
import numpy as np
import pandas as pd
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.utils import save_object
from src.logger import logging
from src.exception import CustomException

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        This method is responsible for data transformation.
        """
        try:
            numeric_features = ["writing_score", "reading_score"]
            categorical_features = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            num_pipeline = Pipeline(
                steps = [
                    ("impute", SimpleImputer(strategy='median')),
                    ("Scaling", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps = [
                    ("impute", SimpleImputer(strategy="most_frequent")),
                    ('encoding', OneHotEncoder()),
                    ('scaling', StandardScaler(with_mean=False))
                ]
            )

            logging.info("Numerical and categorical pipelines created")
            logging.info(f"Numerical features: {numeric_features}")
            logging.info(f"Categorical features: {categorical_features}")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numeric_features),
                    ('cat_pipeline', cat_pipeline, categorical_features)
                ]
            )

            return preprocessor
        
        except Exception as e:
            logging.error(f"Error {e}")
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_df_path, test_df_path):
        try:
            train_df = pd.read_csv(train_df_path)
            test_df = pd.read_csv(test_df_path)

            logging.info("Reading training and testing data completed")

            preprocessing_obj = self.get_data_transformer_object()
            logging.info("Obtained preprocessing object")

            target_col = 'math_score'

            input_feature_train_df = train_df.drop(columns=[target_col], axis=1)
            target_feature_train_df = train_df[target_col]

            input_feature_test_df = test_df.drop(columns=[target_col], axis=1)
            target_feature_test_df = test_df[target_col]

            logging.info("Applying preprocessing object on training and testing dataframes")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            logging.info("Saved Processing object")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            logging.error(f"Error: {e}")
            raise CustomException(e, sys)
