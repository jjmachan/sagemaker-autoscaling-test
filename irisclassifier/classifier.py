# iris_classifier.py
import pandas as pd
from bentoml import BentoService, api, artifacts, env
from bentoml.adapters import DataframeInput
from bentoml.frameworks.sklearn import SklearnModelArtifact


@env(infer_pip_packages=True)
@artifacts([SklearnModelArtifact("model")])
class IrisClassifier(BentoService):
    """
    A minimum prediction service exposing a Scikit-learn model
    """

    @api(input=DataframeInput(), batch=True)
    def predict(self, df: pd.DataFrame):
        """
        An inference API named `predict` with Dataframe input adapter, which codifies
        how HTTP requests or CSV files are converted to a pandas Dataframe object as the
        inference API function input
        """
        return self.artifacts.model.predict(df)

    @api(input=DataframeInput(), batch=True)
    def nextpredict(self, df: pd.DataFrame):
        """
        Another function to have 2 API endpoints.
        TODO: try out other InputHandlers and Models too.
        """
        print("hai there! I'm jithin your worst enemy")
        return self.artifacts.model.predict(df)
