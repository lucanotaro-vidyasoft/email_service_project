import uvicorn
from fastapi import FastAPI
from pkg.controllers.email_controller import router

app = FastAPI(title="L'incredibile inviatore di Email")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)