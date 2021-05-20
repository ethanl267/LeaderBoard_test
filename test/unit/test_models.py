from unittest import TestCase
from website.models import Note,Work,User,Team


class TestModels(TestCase):
    def test_note(self):
        note = Note(data="test", date=20/5/2021, user_id=1)
        self.assertEqual(note.data, "test", "tested")
        self.assertEqual(note.date, 20/5/2021, "tested")
        self.assertEqual(note.user_id, 1, "tested")

    