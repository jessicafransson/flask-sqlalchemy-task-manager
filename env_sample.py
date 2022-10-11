import os 

os.environ.setdefault("IP", "0.0.0.0.")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "any_secret_key")
os.environ.setdefault("DEBUG", "True") # needs to be changed to false before submission
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault("DB_URL", "postgresql:///taskmanager")