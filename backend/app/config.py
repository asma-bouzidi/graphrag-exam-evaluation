import os
from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support"""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )
    
    # OpenAI Configuration (using OpenAI platform directly)
    openai_api_key: str
    openai_model: str = "gpt-4o-mini"
    openai_temperature: float = 0.2
    openai_embedding_model: str = "text-embedding-3-small"
    embedding_dimensions: int = 1536  # text-embedding-3-small default dimensions
    
    # LangSmith Tracing Configuration
    langsmith_tracing: bool = True
    langsmith_endpoint: str = "https://api.smith.langchain.com"
    langsmith_api_key: Optional[str] = None
    langsmith_project: str = "graphrag-exam-evaluation"
    
    # Neo4j Configuration
    neo4j_uri: str = "bolt://localhost:7688"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "exam-secure-password-2024"
    neo4j_database: str = "neo4j"
    
    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8083
    api_workers: int = 4
    log_level: str = "info"
    cors_origins: str = "http://localhost:3004"
    debug: bool = True  # Enable debug mode (shows docs)
    
    # Authentication (optional)
    jwt_secret_key: Optional[str] = "exam-evaluation-secret-key-2024"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Upload Configuration
    max_upload_size_mb: int = 50
    upload_dir: str = "app/uploads"
    
    # Exam Evaluation Configuration
    default_grade_level: int = 6  # 6th grade
    default_subject: str = "mathematics"
    passing_score: float = 50.0  # Minimum passing score
    
    # AI Grading Configuration
    strict_grading: bool = False  # If true, partial credit is reduced
    show_step_by_step: bool = True  # Show step-by-step correction
    
    # Monitoring
    enable_metrics: bool = True
    enable_tracing: bool = True
    
    @property
    def cors_origins_list(self) -> List[str]:
        """Parse CORS origins into a list"""
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    @property
    def max_upload_size_bytes(self) -> int:
        """Convert MB to bytes"""
        return self.max_upload_size_mb * 1024 * 1024


# Global settings instance
settings = Settings()
