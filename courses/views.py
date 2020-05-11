from django.shortcuts import render, get_object_or_404
from .models import Course
from django.views import View
from .forms import CourseForm

# raw versions of generic classes used in blog app and reused here


class CourseUpdateView(View):
    template_name = 'courses/course_update.html'
    def get_object(self):
        _id = self.kwargs.get('id')
        obj = None
        if _id is not None:
            obj = get_object_or_404(Course, id=_id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        form = CourseForm(request.POST)
        if obj is not None:
            form = CourseForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                form = CourseForm()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    def get(self, request, *args, **kwargs):
        form = CourseForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseForm()
        context = {'form': form}
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

# using heritance we can even make it shorter now:
# class MyListView(CourseListView):
#     queryset = Course.objects.filter(id=1)
# if we want choose specyfic item

class CourseDetailView(View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)



def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
