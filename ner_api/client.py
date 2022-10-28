from typing import Dict


class NamedEntityClient:

    def __init__(self, model) -> None:
        self.model = model

    def get_ents(self, sentance: str) -> Dict:
        return {}
