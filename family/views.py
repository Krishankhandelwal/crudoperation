from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,HttpResponseRedirect
from .models import Details
from .forms import DetailsForm
# Create your views here.
def create(request):
    context={}
    form=DetailsForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request,'create.html',context)


def list(request):
    context={}
    context['dataset']=Details.objects.all()
    return render(request,'list.html',context)

def detail(request,id):
    contest={}
    contest['data']=Details.objects.get(id=id)
    return render(request,'detail.html',contest)

def update_view(request, pk):
    obj = get_object_or_404(Details, pk=pk)

    if request.method == 'POST':
        form = DetailsForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DetailsForm(instance=obj)

    context = {'form': form}
    return render(request, 'update.html', context)


def delete(request, id):
    context ={}
    obj = get_object_or_404(Details, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "delete.html", context)

