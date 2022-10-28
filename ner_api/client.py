from typing import Dict, Optional


class NamedEntityClient:

    def __init__(self, model) -> None:
        self.model = model

    def get_ents(self, sentance: str) -> Dict:
        doc = self.model(sentance)
        entities = [{'ent': ent.text, 'label': map_label(ent.label_)}
                    for ent in doc.ents]
        return {'ents': entities, 'html': []}


def map_label(label: str) -> Optional[str]:
    label_map = {
        'PERSON': 'Person',
        'NORP': 'Group',
        'LOC': 'Location',
        'GPE': 'Location',
        'LANGUAGE': 'Language'
    }
    return label_map.get(label)
