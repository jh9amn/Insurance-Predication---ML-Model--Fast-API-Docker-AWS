# Importing the model
from typing import Literal, Annotated
import pickle
import pandas as pd

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

## Manually added model version for tracking purposes. In production, this should be automated via CI/CD pipelines and version control.
MODEL_VERSION = "1.0.0"  

## Get class labels for reference (if needed for post-processing or API documentation)
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])
    
    predicted_class = model.predict(input_df)[0]
    
    # Get probability of the all predicted class
    pribabilities = model.predict_proba(input_df)[0]
    confidence = max(pribabilities)
    
    ## Create mapping: {class_label: probability}
    class_prob_mapping = dict(zip(class_labels, map(lambda x: round(x, 4), pribabilities)))
    
    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4), 
        "class_probabilities": class_prob_mapping
    }