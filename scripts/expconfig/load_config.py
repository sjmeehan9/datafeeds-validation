import os
import yaml

def config_loader() -> dict:
    config_file_path = os.path.join(os.path.dirname(__file__), "locconfig.yml")

    try:
        with open(config_file_path, 'r') as f:
            config = yaml.safe_load(f)
            return config
    except FileNotFoundError:
        raise Exception("Config file not found")
    except yaml.parser.ParserError as exc:
        raise Exception(f"Error parsing YAML: {exc}")