from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import MODEL_VERSION, predict_output
from schema.predict_response import PredictResponse
from schema.user_input import UserInput
    
app = FastAPI()
        
## Huamn readable descriptions for API documentation
@app.get("/")
def read_root():
    return {"message": "Welcome to the Insurance Premium Prediction API. Use the /predict endpoint to get your premium estimate."}

## Mach
@app.get("/health")
def health_check():
    return {"status": "API is healthy and running.",
            "model_version": MODEL_VERSION}
        
@app.post("/predict", response_model=PredictResponse, summary="Predict Insurance Premium Category", description="Provide user details to get the predicted insurance premium category along with confidence and class probabilities.")
def predict(data: UserInput):
    
    user_input = {
        
            "bmi": data.bmi,
            "age_group": data.age_group,
            "lifestyle_risk": data.lifestyle_risk,
            "income_lpa": data.income_lpa,
            "city_tier": data.city_tier,
            "occupation": data.occupation
        
    }
    
    try:
        prediction = predict_output(user_input)
        return JSONResponse(content={"response": prediction}, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)