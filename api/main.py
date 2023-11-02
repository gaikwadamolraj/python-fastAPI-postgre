# import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from routes.metadataRequests import router
from schemas.metadataModels import HealthResponse

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router, prefix="/api/v1/metadata")

@app.get("/", status_code=status.HTTP_200_OK, response_model=HealthResponse)
async  def health():
    return HealthResponse(status="OK")

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
