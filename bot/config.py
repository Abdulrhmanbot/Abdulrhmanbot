import os


class Config:

    BOT_TOKEN = "5720599238:AAGAir604n4d8n3x8s1GlnSdxjQ2HuXYIVM"

    SESSION_NAME = ":memory:"

    API_ID = "20620984"

    API_HASH = "7a710d252533a33b7db67fc42d62a1b6"

    CLIENT_ID = "814700032498-710erok2296p0182aqraml1avkfmn0su.apps.googleusercontent.com"

    CLIENT_SECRET = "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"

    BOT_OWNER = "5956062507"

    AUTH_USERS_TEXT = "5956062507"

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = "public"
    
    CRED_FILE = "auth_token.txt"
