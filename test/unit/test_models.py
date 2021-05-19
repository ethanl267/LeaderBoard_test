from unittest import TestCase
from flask import models


class Note(TestCase.unittest):
    def test_create_models(self):
        Note = Note(id=1)

        self.assertEqual(Note)