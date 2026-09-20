from django.shortcuts import get_object_or_404, render
from .models import Course, Lesson
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'courses/home.html')


@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lesson_set.all()

    return render(
        request,
        'courses/course_detail.html',
        {'course': course, 'lessons': lessons}
    )


def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    return render(
        request,
        'courses/lesson_detail.html',
        {'lesson': lesson}
    )