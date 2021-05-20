from unittest import TestCase
from website.models import Note,Work,User,Team


class TestModels(TestCase):
    def test_note(self):
        note = Note(data="test", date=20/5/2021, user_id=1)
        self.assertEqual(note.data, "test", "tested")
        self.assertEqual(note.date, 20/5/2021, "tested")
        self.assertEqual(note.user_id, 1, "tested")

class TestModels(TestCase):
    def test_Work(self):
        work = Work(user_id=1, date=20/5/2021, title="test", description="test", status="test", point="test")
        self.assertEqual(work.user_id, 1, "tested")
        self.assertEqual(work.date, 20/5/2021, "tested")
        self.assertEqual(work.title, "test", "tested")
        self.assertEqual(work.description, "test", "tested")
        self.assertEqual(work.status, "test", "tested")
        self.assertEqual(work.points, "test", "tested")

class TestModels(TestCase):
    def test_User(self):
        user = User(team_id=1, email="test", password="test", first_name="test", notes="test", team_leader="test", work="test", points="test")
        self.assertEqual(user.team_id, 1, "tested")
        self.assertEqual(user.email, "test", "tested")
        self.assertEqual(user.password, "test", "tested")
        self.assertEqual(user.first_name, "test", "tested")
        self.assertEqual(user.notes, "test", "tested")
        self.assertEqual(user.team_leader, "test", "tested")
        self.assertEqual(user.work, "test", "tested")
        self.assertEqual(user.points, "test", "tested")

class TestModels(TestCase):
    def test_team(self):
        team = Team(name="test")
        self.assertEqual(team.name, "test", "tested")


    