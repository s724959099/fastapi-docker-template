from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import os
from log import logger, setup_logging

DEBUG = os.environ.get('ENV')
app = FastAPI()
app.debug = DEBUG
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()


@app.get('/')
def index():
    res = dict(data='ok')
    return JSONResponse(content=jsonable_encoder(res))


@app.on_event("startup")
async def startup():
    logger.info('before startup')
    setup_logging()


if __name__ == '__main__':
    if DEBUG:
        uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=False, workers=1)
