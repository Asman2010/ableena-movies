from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import tamilmv, piratebay

# Create FastAPI app
app = FastAPI(
    title="Movie Streamer API",
    description="API for searching and streaming movies from various sources",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tamilmv.router)
app.include_router(piratebay.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Movie Streamer API",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
