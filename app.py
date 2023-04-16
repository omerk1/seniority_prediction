import uvicorn
from fastapi import FastAPI

import src.app_config as config
from src.seniority_prediction import predict_seniority

app = FastAPI()


@app.post("/predict")
def predict(title: str):
    pred = predict_seniority(title=title)
    resp = {"prediction": pred}
    return resp


if __name__ == '__main__':
    uvicorn.run(app, host=config.HOST, port=int(config.PORT))
