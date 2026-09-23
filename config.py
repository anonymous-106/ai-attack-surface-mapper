class Config:
    APP_NAME = "AI Attack Surface Mapper"
    ENVIRONMENT = "development"
    LOG_LEVEL = "INFO"

    #TARGET CONFIGURATION
    ALLOWED_TARGET_TYPES = ("DOMAIN", "IP_ADDRESS", "URL")
    REQUIRED_EXPLICIT_SCOPE = True