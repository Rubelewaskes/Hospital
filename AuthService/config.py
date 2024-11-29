from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent

class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "auth" / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "auth" / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expiere_minutes: int = 3

class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    auth_jwt: AuthJWT = AuthJWT()

settings = Settings()