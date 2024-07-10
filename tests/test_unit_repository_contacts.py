import unittest
from unittest.mock import patch
from repository.tasks import TaskRepository

class TestTaskRepository(unittest.TestCase):
    def setUp(self):
        self.repository = TaskRepository()

    def test_create_task(self):
        task = {'title': 'Finish homework', 'description': 'Complete all tasks for the week', 'due_date': '2024-07-15'}
        created_task = self.repository.create_task(task)
        self.assertIsNotNone(created_task)
        self.assertEqual(created_task['title'], 'Finish homework')
        self.assertEqual(created_task['description'], 'Complete all tasks for the week')
        self.assertEqual(created_task['due_date'], '2024-07-15')

    def test_get_all_tasks(self):
        tasks = self.repository.get_all_tasks()
        self.assertIsInstance(tasks, list)

    def test_get_task_by_id(self):
        task = {'title': 'Finish homework', 'description': 'Complete all tasks for the week', 'due_date': '2024-07-15'}
        created_task = self.repository.create_task(task)
        retrieved_task = self.repository.get_task_by_id(created_task['id'])
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task['title'], 'Finish homework')
        self.assertEqual(retrieved_task['description'], 'Complete all tasks for the week')
        self.assertEqual(retrieved_task['due_date'], '2024-07-15')

    def test_update_task(self):
        task = {'title': 'Finish homework', 'description': 'Complete all tasks for the week', 'due_date': '2024-07-15'}
        created_task = self.repository.create_task(task)
        updated_task = {'title': 'Finish all homework', 'description': 'Complete all tasks for the week and weekend', 'due_date': '2024-07-20'}
        self.repository.update_task(created_task['id'], updated_task)
        retrieved_task = self.repository.get_task_by_id(created_task['id'])
        self.assertEqual(retrieved_task['title'], 'Finish all homework')
        self.assertEqual(retrieved_task['description'], 'Complete all tasks for the week and weekend')
        self.assertEqual(retrieved_task['due_date'], '2024-07-20')

    def test_delete_task(self):
        task = {'title': 'Finish homework', 'description': 'Complete all tasks for the week', 'due_date': '2024-07-15'}
        created_task = self.repository.create_task(task)
        self.repository.delete_task(created_task['id'])
        retrieved_task = self.repository.get_task_by_id(created_task['id'])
        self.assertIsNone(retrieved_task)