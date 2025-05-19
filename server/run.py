from fastapi import FastAPI
from utils.config import Config
from utils.route import router
import uvicorn

app = FastAPI()
config = Config('config/config.json')

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'run:app', 
        host=config.host,
        port=config.port,
        reload=True
        )
