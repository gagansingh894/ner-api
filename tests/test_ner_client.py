from re import S
import unittest
from ner_api.client import NamedEntityClient


class TestNerClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_input(self):
        model = NerModelTestDouble('eng')
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def tests_get_ents_returns_list_given_nonempty_string(self):
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Mumbai is a city in India")
        self.assertIsInstance(ents, dict)
