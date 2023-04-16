import uvicorn
from fastapi import FastAPI

from src.seniority_prediction import predict_seniority

app = FastAPI()


@app.get("/predict")
def predict(title: str):
    pred = predict_seniority(title=title)
    resp = {"prediction": pred}
    return resp


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)
