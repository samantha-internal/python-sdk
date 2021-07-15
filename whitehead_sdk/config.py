import os


API_ENDPOINT = os.environ.get("WHITEHEAD_API_ENDPOINT", "https://api.whitehead.cloud/v1/graphql")
AUTH_ENDPOINT = os.environ.get("WHITEHEAD_AUTH_ENDPOINT", "https://sdk.whitehead.cloud/generateHasuraJWT")
