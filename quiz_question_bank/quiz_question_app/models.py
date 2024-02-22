from django.db import models
from uuid import uuid4

class Question(models.Model):
    """
    Model to store quiz questions
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    question_text = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.question_text

class Option(models.Model):
    """
    Model to store options for a question
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    choice = models.CharField(max_length=1)
    option_text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        """A string representation of the model."""
        return f"{self.question} - Option {self.choice} - {self.option_text}"

class Answer(models.Model):
    """
    Model to store answers for a question
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    question = models.ForeignKey(Question, related_name="answer", on_delete=models.CASCADE)
    selected_choice = models.CharField(max_length=1)
    answer = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return f"{self.question} - Selected: {self.selected_choice} {self.answer}"