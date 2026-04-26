from pydantic import BaseModel, Field
from typing import Dict

class PredictResponse(BaseModel):
    predicted_category: str = Field(..., description="The predicted insurance premium category", examples=["High"])
    confidence: float = Field(..., description="Confidence score of the prediction (0 to 1)", examples=[0.85])
    class_probabilities: Dict[str, float] = Field(..., description="Mapping of each class label to its predicted probability", examples=[{"Low": 0.05, "Medium": 0.10, "High": 0.85}])