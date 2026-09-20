from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'courses/home.html')

@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.get_or_create(
        user=request.user,
        course=course
    )

    return redirect('course_detail', course_id=course.id)

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    enrolled = Enrollment.objects.filter(
        user=request.user,
        course=course
    ).exists()

    lessons = course.lesson_set.all() if enrolled else []

    return render(
        request,
        'courses/course_detail.html',
        {
            'course': course,
            'lessons': lessons,
            'enrolled': enrolled,
        }
    )

@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    enrolled = Enrollment.objects.filter(
        user=request.user,
        course=lesson.course
    ).exists()

    if not enrolled:
        return redirect('course_detail', course_id=lesson.course.id)

    return render(
        request,
        'courses/lesson_detail.html',
        {'lesson': lesson}
    )

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(
        user=request.user
    ).select_related('course')

    courses = [enrollment.course for enrollment in enrollments]

    return render(
        request,
        'courses/my_courses.html',
        {'courses': courses}
    )