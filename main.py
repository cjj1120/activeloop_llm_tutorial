from dotenv import load_dotenv

x = load_dotenv("./.env")  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

import os

open_ai_acc = os.environ.get("open_ai_acc")
print(open_ai_acc) # tested 👍

