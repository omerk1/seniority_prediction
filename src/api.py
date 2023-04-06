import uvicorn
from fastapi import FastAPI

import api_config

app = FastAPI()


@app.post("/predict")
def predict(title: str):
    pred = title == 'vp'
    resp = {"prediction": pred}
    return resp


if __name__ == '__main__':
    uvicorn.run(app, host=api_config.HOST, port=int(api_config.PORT))
