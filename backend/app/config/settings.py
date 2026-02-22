from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "India Climate Intelligence"
    DEBUG: bool = True
    
    # Hadoop / DB Settings (To be filled by DB Team)
    HADOOP_HOST: str = "localhost"
    HADOOP_PORT: int = 10000
    HIVE_DATABASE: str = "climate_db"
    
    # ML Settings (To be filled by ML Team)
    MODEL_PATH: str = "ml/saved_models/forecast_model.pkl"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()