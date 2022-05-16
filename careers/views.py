from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Jobs, Application
from .forms import JobsForm, ApplicationForm

# Create your views here.
def careers(request):
    jobinstances = Jobs.objects.all()
    context = {
        'jobinstances':jobinstances,
    }
    return render(request, 'careers/careers.html', context)

def getjobform(request):
    form = JobsForm
    context = {
        'form':form,
    }
    return render(request, 'careers/jobform.html', context)

def postjobform(request):
    form = JobsForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('adminArea')

def getapplicationform(request, form_id):
    jinstance = get_object_or_404(Jobs, pk=form_id)
    ainstances = Application.objects.all().filter(id=form_id)
    form = ApplicationForm
    context = {
        'jinstance':jinstance,
        'ainstances':ainstances,
        'form':form,
    }
    return render(request, 'careers/applicationform.html', context)

def postapplicationform(request, form_id):
    form = ApplicationForm(request.POST, request.FILES)
    form.instance.job = get_object_or_404(Jobs,pk=form_id)
    if request.user.is_authenticated:
        form.instance.user_id = request.user.id
        has_application = Application.objects.all().filter(user_id=form.instance.user_id,job=form.instance.job)
        if has_application:
            return redirect('dashboard')
        else:
            if form.is_valid():
                form.save()
                return redirect('dashboard')
            else:
                return redirect('index')

def viewappcategory(request):
    jinstances = Jobs.objects.all()
    context={
        'jinstances':jinstances,
    }
    return render(request, 'careers/application_category.html', context)

def viewapplications(request, job_id):
    jinstance = get_object_or_404(Jobs,pk=job_id)
    ainstances = Application.objects.all().filter(job=jinstance)
    context={
        'jinstance':jinstance,
        'ainstances':ainstances,
    }
    return render(request, 'careers/jobapplications.html', context)

def viewapplication(request, job_id, app_id):
    ainstance = get_object_or_404(Application, pk=app_id)
    jinstance = get_object_or_404(Jobs,pk=job_id)
    context = {
        'ainstance':ainstance,
        'jinstance':jinstance,
    }
    return render(request, 'careers/jobapplication.html', context)

def reviewed(request, job_id, app_id):
    ainstance = get_object_or_404(Application, pk=app_id)
    if ainstance.reviewed == False:
        ainstance.reviewed = True
    else:
        ainstance.reviewed = False
    ainstance.save()
    return redirect('/careers/viewappcategory/'+str(job_id)+'/'+str(app_id))

def accepted(request, job_id, app_id):
    ainstance = get_object_or_404(Application, pk=app_id)
    if ainstance.accepted == False:
        ainstance.accepted = True
        if ainstance.reviewed == False:
            ainstance.reviewed = True
    else:
        ainstance.accepted = False
    ainstance.save()
    return redirect('/careers/viewappcategory/'+str(job_id)+'/'+str(app_id))