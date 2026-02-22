from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.routes import forecast, anomaly, severity

# --- Lifespan Logic (Modern Replacement for on_event) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # [STARTUP] Everything here runs when the server starts
    print("🚀 System Starting: Loading ML Models into memory...")
    # Example: app.state.model = joblib.load("path/to/model.pkl")
    
    yield  # The application runs while this is suspended
    
    # [SHUTDOWN] Everything here runs when the server stops
    print("🛑 System Shutting Down: Cleaning up resources...")

# --- Initialize App ---
app = FastAPI(
    title="India Climate Intelligence System API",
    description="AI-powered climate forecasting and severity analysis",
    version="1.0.0",
    lifespan=lifespan
)

# --- Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Include Routers ---
app.include_router(forecast.router, prefix="/api/v1/climate", tags=["Forecasting"])
app.include_router(anomaly.router, prefix="/api/v1/climate", tags=["Anomaly Detection"])
app.include_router(severity.router, prefix="/api/v1/climate", tags=["Severity Scoring"])

@app.get("/")
async def health_check():
    return {
        "status": "online", 
        "message": "India Climate Intelligence System is active",
        "docs": "/docs"
    }