class Config:
    DB_URL = (
        "postgresql+asyncpg://postgres:mysecretpassword@localhost:5432/contacts_app"
    )


config = Config