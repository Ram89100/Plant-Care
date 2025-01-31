from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from services import load_model, predict_disease, num_classes
from assets.disease_descriptions import disease_descriptions

app = FastAPI()

# Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model once during startup
plant_disease_model = load_model()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Plant Disease Prediction API!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        if file.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(status_code=400, detail="Invalid file type. Please upload a JPEG or PNG image.")

        image_bytes = await file.read()

        # Perform prediction
        prediction = predict_disease(image_bytes, plant_disease_model, num_classes, disease_descriptions)

        # Response payload
        response = {
            "prediction": prediction["class"],  # Class name predicted
            "description": prediction["description"],  # Description of the disease
        }

        return JSONResponse(content=response)

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
