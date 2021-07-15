import os


def main():
    os.system("gql-compiler whitehead_sdk/schema/ whitehead_sdk/api/ --config_path whitehead_sdk/schema_config/json_scalar.py")
