import logging

from fastapi import FastAPI, Path, status
from fastapi.responses import JSONResponse

app = FastAPI(docs_url=None, redoc_url="/docs")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@app.on_event("startup")
def init_config():
    logger.info("Initialising config..")


@app.get("/", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def health_check():
    return JSONResponse({"Status": "Healthy as a fish"})


@app.post("/{datastream}", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def send_message(
    datastream: str = Path(..., title="Example datastream as route param"),
) -> JSONResponse:
    logger.info("Received post request for datastream: %s", datastream)
    return JSONResponse({"status": "message received"})
