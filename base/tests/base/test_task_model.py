from django.test import TestCase
from django.contrib.auth.models import User
from ...models import Task

class TaskModelTestCase(TestCase):
    def setUp(self):
        # Configuração inicial 
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(user=self.user, title='Test Task', description='This is a test task')

    def test_task_creation(self):
        # Testa se a tarefa é criada corretamente
        task_count = Task.objects.count()
        self.assertEqual(task_count, 1)

    def test_task_str(self):
        # Testa se o método __str__ retorna o título da tarefa
        self.assertEqual(str(self.task), 'Test Task')

    def test_task_user_association(self):
        # Testa se a tarefa está associada corretamente ao usuário
        self.assertEqual(self.task.user, self.user)

    def test_task_complete_default(self):
        # Testa se o status de conclusão padrão de uma tarefa é False
        self.assertFalse(self.task.complete)

    def test_task_description_optional(self):
        # Testa se a descrição de uma tarefa pode ser opcional 
        task_without_description = Task.objects.create(user=self.user, title='Task without Description')
        self.assertIsNone(task_without_description.description)

    def test_task_created_auto_now_add(self):
        # Testa se o campo 'created' é preenchido automaticamente com a data/hora atual na criação da tarefa
        task_with_auto_created = Task.objects.create(user=self.user, title='Task with Auto Created')
        self.assertIsNotNone(task_with_auto_created.created)

