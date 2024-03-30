from django.test import TestCase
from django.contrib.auth.models import User
from ...models import Task

class TaskIntegrationTestCase(TestCase):
    def setUp(self):
        # Configuração inicial 
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_task(self):
        # Testa a criação de uma nova tarefa no banco de dados
        initial_task_count = Task.objects.count()
        Task.objects.create(user=self.user, title='New Task', description='This is a new task')
        new_task_count = Task.objects.count()
        self.assertEqual(new_task_count, initial_task_count + 1)

    def test_delete_task(self):
        # Testa a exclusão de uma tarefa do banco de dados
        task = Task.objects.create(user=self.user, title='Task to Delete', description='This is a task to delete')
        initial_task_count = Task.objects.count()
        task.delete()
        new_task_count = Task.objects.count()
        self.assertEqual(new_task_count, initial_task_count - 1)

    
