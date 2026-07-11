from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import uvicorn
import os

from text_summarizer.pipeline.prediction import PredictionPipeline


app = FastAPI()


class TextRequest(BaseModel):
    text: str


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return {"message": "Training successful !!"}

    except Exception as e:
        return {"error": str(e)}


@app.post("/predict")
async def predict_route(request: TextRequest):
    try:
        obj = PredictionPipeline()

        summary = obj.predict(request.text)

        return {
            "summary": summary
        }

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 2122))
    uvicorn.run(app, host="0.0.0.0", port=port)