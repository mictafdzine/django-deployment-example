from django.shortcuts import render

# Create your views here.
def HomePage(request):
    context_dict = {'text':'hello world','number':100}
    return render(request, 'basicapp/homepage.html',context_dict)

def Other(request):
    return render(request, 'basicapp/other.html')


def relative_url_templates(request):
    return render(request,'basicapp/relative_url_templates.html')
