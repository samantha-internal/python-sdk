import os


API_ENDPOINT = os.environ.get("WHITEHEAD_API_ENDPOINT", "https://api.whitehead.ai/hasura/v1/graphql")
AUTH_ENDPOINT = os.environ.get("WHITEHEAD_AUTH_ENDPOINT", "https://auth.whitehead.ai/generateHasuraJWT")
