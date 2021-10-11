"""
Labs DS Machine Learning Operations Role
- Application Programming Interface
"""
import json

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.data import Data
from app.model import Model

API = FastAPI(
    title='Lambda School Labs Data Science API',
    version="0.0.1",
    docs_url='/',
)
API.data = Data()
API.model = Model.load()


@API.get("/data/")
async def data():
    return API.data.rows()


@API.get("/data/count/")
async def data_count():
    return {"Row Count": API.data.count()}


@API.post("/data/insert/")
async def data_insert(feature_1: int = Form(...),
                      feature_2: int = Form(...),
                      feature_3: int = Form(...),
                      target: str = Form(...)):
    idx = API.data.insert(feature_1, feature_2, feature_3, target)
    return API.data.row(idx)


@API.post("/data/seed/")
async def data_seed(num: int = Form(...)):
    magnitude = abs(num)
    if num > 0:
        API.data.seed(magnitude)
    elif num < 0:
        API.data.reset()
        API.data.seed(magnitude)
    else:
        API.data.reset()
    return {
        "Seeds Added": magnitude,
        "Total Rows": API.data.count(),
    }


@API.get("/model/")
async def model():
    return API.model.info


@API.get("/model/train/")
async def model_train():
    API.model = Model()
    return API.model.info


@API.post("/model/predict/")
async def model_predict(feature_1: int = Form(...),
                        feature_2: int = Form(...),
                        feature_3: int = Form(...)):
    prediction, confidence = API.model(feature_1, feature_2, feature_3)
    return {
        "Prediction": prediction,
        "Confidence": confidence,
    }


@API.post("/vis/class-by-feature/")
def class_by_feature(feature_id: int = Form(...)):
    return json.loads(
        API.data.crosstab_vis(feature_id).to_json()
    )


@API.post("/vis/class-by-percent/")
def class_by_percent():
    return json.loads(
        API.data.target_percent_vis().to_json()
    )


API.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(API)
