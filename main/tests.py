from django.test import TestCase
from main.models import Board, Thread, User, Role, University, Reply

# Create your tests here.
class DatabaseTest(TestCase):
    def setUp(self):
        self.sample_board = Board.objects.create(board_id="pup", name="Polytecnic Universitiy of The Philippines")
        self.sample_role = Role.objects.create(name="User")
        self.sample_uni = University.objects.create(
            university_id = "pup",
            name = "Polytecnic Universitiy of The Philippines",
            verified = True
        )
        self.sample_user = User.objects.create(
            username="Anonymous",
            password="test",
            role=self.sample_role,
            university=self.sample_uni
        )
        self.sample_thread = Thread.objects.create(
            title="Title 1",
            board=self.sample_board,
            username=self.sample_user,
            body="This is a body from Title 1"
        )
        self.sample_reply = Reply.objects.create(
            username=self.sample_user,
            thread=self.sample_thread,
            body="This is a reply.",
        )
        self.sample_reply_2 = Reply.objects.create(
            username=self.sample_user,
            thread=self.sample_thread,
            body="This is another reply.",
        )

    def test_search_ids(self):
        self.assertEqual(Board.objects.filter(board_id="pup")[0].board_id, 'pup', "pup is not found!")
        self.assertEqual(Role.objects.filter(name="User")[0].name, 'User', "User Role is not found!")
        self.assertEqual(University.objects.filter(university_id="pup")[0].university_id, 'pup', "pup is not found!")
        self.assertEqual(User.objects.filter(username="Anonymous")[0].username, 'Anonymous', "anon is not found!")
        self.assertEqual(Thread.objects.filter(username="Anonymous")[0].username.username, 'Anonymous', "anon is not found!")
        self.assertEqual(Reply.objects.filter(id=1)[0].id, 1, "post not found!")
        self.assertEqual(Reply.objects.filter(id=2)[0].body, "This is another reply.", "post not found!")
        
class BoardTest(TestCase):
    def setUp(self):
        Board.objects.create(board_id="pup", name="Polytecnic Universitiy of The Philippines")
        Board.objects.create(board_id="up", name="Universitiy of The Philippines")
        Board.objects.create(board_id="tip", name="Technological Institute of The Philippines")

    def test_get_board(self):
        board = Board.objects.get(board_id='pup')
        self.assertEqual(board.board_id, 'pup', "pup is not found!")
        with self.assertRaises(Board.DoesNotExist, msg="ust randomly found"):
            Board.objects.get(board_id='ust')

    def test_get_all_boards(self):
        boards = Board.objects.all()
        self.assertEqual(boards[0].board_id, 'pup', "pup is not found!")
        self.assertEqual(boards[1].board_id, 'up', "up is not found!")

        self.assertNotEqual(boards[2].board_id, 'ust', "ust is randomly found!")

class ThreadTest(TestCase):
    def setUp(self):
        Board.objects.create(board_id="pup", name="Polytecnic Universitiy of The Philippines")
        Board.objects.create(board_id="up", name="Universitiy of The Philippines", description="“Honor, Excellence, Service”")
        Board.objects.create(board_id="tip", name="Technological Institute of The Philippines")

        Role.objects.create(name="User")

        University.objects.create(
            university_id = "pup",
            name = "Polytecnic Universitiy of The Philippines",
            verified = True
        )

        User.objects.create(
            username="Anonymous",
            password="test",
            role=Role.objects.get(name="User"),
            university=University.objects.get(university_id="pup")
        )

        Thread.objects.create(
            title="Title 1",
            board=Board.objects.get(board_id="pup"),
            username=User.objects.get(username="Anonymous"),
            body="This is a body from Title 1"
        )

        Thread.objects.create(
            title="Title 2",
            board=Board.objects.get(board_id="up"),
            username=User.objects.get(username="Anonymous"),
            body="This is a body from Title 2"
        )

        Thread.objects.create(
            title="Title 3",
            board=Board.objects.get(board_id="pup"),
            username=User.objects.get(username="Anonymous"),
            body="This is a body from Title 3"
        )
        

    def test_get_threads_from_board(self):
        threads = Thread.objects.filter(board=Board.objects.get(board_id="pup"))

        self.assertEqual(threads[0].board, Board.objects.get(board_id="pup"), "the thread is not from a pup board")
        self.assertEqual(threads[0].title, 'Title 1', "the thread is not the first entry")
        self.assertNotEqual(threads[1].board, Board.objects.get(board_id="up"), "thread is not from up board")
        self.assertEqual(threads[1].title, "Title 3", "thread is not the second thread from pup board")

    # def test_add_reply