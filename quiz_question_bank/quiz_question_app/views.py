import logging.config
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from .models import Question, Option, Answer
import json
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger(__name__)


@csrf_exempt
def create_question(request):
    """
    Create a new question with options and answers
    """
    # Get the JSON data from the request body
    try:
        data = json.loads(request.body.decode('utf-8'))

        # Extract question_text, options, and answer from the JSON data
        question_text = data.get('question_text')
        options_data = data.get('options', [])
        answer_data = data.get('answer')

        # Create the question
        question = Question.objects.create(question_text=question_text)

        # Create the options and associate them with the question
        for option_data in options_data:
            choice, option_text = list(option_data.keys())[
                0], list(option_data.values())[0]
            is_correct = option_data.get('is_correct', False)

            Option.objects.create(
                question=question,
                choice=choice,
                option_text=option_text,
                is_correct=is_correct
            )

        # Create the correct answer
        correct_option_choice = list(answer_data.keys())[0]
        correct_option = Option.objects.get(
            question=question, choice=correct_option_choice)
        Answer.objects.create(
            question=question,
            selected_choice=correct_option_choice,
            answer=correct_option.option_text
        )

        return JsonResponse({
            'message': 'Question created successfully',
            'question_id': question.id}, status=status.HTTP_201_CREATED
        )
    except Exception as e:
        logger.error(f"Error creating question: {str(e)}")
        return HttpResponseServerError({'message': 'Error creating question'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@require_http_methods(["GET"])
@csrf_exempt
def get_questions(request):
    """
    Get all questions with options and answers
    """
    try:
        questions = Question.objects.all()
        questions_data = []

        for question in questions:
            options = Option.objects.filter(question=question)
            options_data = []

            for option in options:
                options_data.append({
                    option.choice: option.option_text
                })

            answer = Answer.objects.get(question=question)
            answer_data = {
                answer.selected_choice: answer.answer
            }

            questions_data.append({
                'question_id': question.id,
                'question_text': question.question_text,
                'options': options_data,
                'answer': answer_data
            })
        return JsonResponse({
            'message': 'Questions retrieved successfully',
            'questions': questions_data}, status=status.HTTP_200_OK
        )
    except Question.DoesNotExist:
        return HttpResponseNotFound(
            {'message': 'Questions not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        logger.error(f"Error getting questions: {str(e)}")
        return HttpResponseServerError({'message': 'Error getting questions'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@require_http_methods(["GET"])
def get_question(request, question_id):
    """
    Get a question with options and answers
    """
    try:
        question = Question.objects.get(id=question_id)
        options = Option.objects.filter(question=question)
        options_data = []

        for option in options:
            options_data.append({
                option.choice: option.option_text
            })

        answer = Answer.objects.get(question=question)
        answer_data = {
            answer.selected_choice: answer.answer
        }

        return JsonResponse({
            'message': 'Question retrieved successfully',
            'question_text': question.question_text,
            'options': options_data,
            'answer': answer_data
        }, status=status.HTTP_200_OK)

    except Question.DoesNotExist:
        return HttpResponseNotFound(
            {'message': 'Question not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        logger.error(f"Error getting question: {str(e)}")
        return HttpResponseServerError({'message': 'Error getting question'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_question(request, question_id):
    """
    Delete a question with options and answers
    """
    try:
        #  Check if the request has the HTTP_AUTHORIZATION header to ensure the user is authenticated
        if 'HTTP_AUTHORIZATION' not in request.META:
            return JsonResponse({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        question = get_object_or_404(Question, id=question_id)
        question.delete()
        return JsonResponse({'message': f'Question with id {question_id} deleted successfully'}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Error deleting question: {str(e)}")
        return HttpResponseServerError({'message': 'Error deleting question'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_all_questions(request):
    """
    Delete all questions with options and answers
    """
    try:
        #  Check if the request has the HTTP_AUTHORIZATION header to ensure the user is authenticated
        if 'HTTP_AUTHORIZATION' not in request.META:
            return JsonResponse({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        Question.objects.all().delete()
        return JsonResponse({'message': 'All questions deleted successfully'}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Error deleting all questions: {str(e)}")
        return HttpResponseServerError({'message': 'Error deleting all questions'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@require_http_methods(["PUT"])
def update_question(request, question_id):
    """
    Update a question with options and answers,
    Can also update each part of the question separately
    """
    try:
        question = get_object_or_404(Question, id=question_id)
        data = json.loads(request.body.decode('utf-8'))

        question.question_text = data.get(
            'question_text', question.question_text)
        question.save()

        options_data = data.get('options', [])
        answer_data = data.get('answer')

        # Update the options and associate them with the question
        if options_data:
            for option_data in options_data:
                choice, option_text = list(option_data.keys())[
                    0], list(option_data.values())[0]
                is_correct = option_data.get('is_correct', False)

                Option.objects.update_or_create(
                    question=question,
                    choice=choice,
                    defaults={'option_text': option_text,
                              'is_correct': is_correct}
                )

        # Update the correct answer
        if answer_data:
            correct_option_choice = list(answer_data.keys())[0]
            correct_option = Option.objects.get(
                question=question, choice=correct_option_choice)
            Answer.objects.update_or_create(
                question=question,
                defaults={'selected_choice': correct_option_choice,
                          'answer': correct_option.option_text}
            )

        return JsonResponse({'message': f'Question with id {question_id} updated successfully'}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Error updating question: {str(e)}")
        return HttpResponseServerError({'message': 'Error updating question'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
