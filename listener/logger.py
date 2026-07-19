import json
import os
from listener.schema import Interaction

LOG_FILE = os.path.join("logs", "interactions.jsonl")

def log_interaction(interaction: Interaction) -> None:
    """
    Appends a single interaction as one JSON line to the log file.
    Creates the logs/folder and a file if they don't exist yet.
    """

    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(interaction.to_dict()) + "\n")


