from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Topic, Webpage

# Create your views here.


def form1(request):
    if request.method == "POST":
        # return HttpResponse(request.POST['First Name'])
        print(request.POST.get("name"))
        print(request.POST.get("emailid"))
        print(request.POST.get("phno"))
        print(request.POST.get("gender"))
    return render(request, "form1.html")


def form2(request):
    # if request.method=="POST":
    # print(request.POST.getlist("hobby"))
    # print(request.POST.getlist("fav"))
    return render(request, "form2.html")


def resp(request):
    # return HttpResponse("Control came to response")
    data = {}
    if request.method == "POST":
        data = dict(request.POST)
        data.pop("csrfmiddlewaretoken")
    return render(request, "resp.html", {'data': data})


def add_topic(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        t = Topic.objects.create(top_name=topic)
        t.save()
        return HttpResponse("<h1>Topic Added Successfully</h1>")
    return render(request, "create_topic.html")


def create_webpage(request):
    topics = Topic.objects.all()
    return render(request, "create_webpage.html", {"topics": topics})


def add_webpage(request):
    topic = request.POST.get("topic")
    name = request.POST.get("name")
    url = request.POST.get("url")
    t = Topic.objects.get_or_create(top_name=topic)[0]
    w = Webpage.objects.create(topic=t, name=name, url=url)
    t.save()
    w.save()
    return HttpResponse("webpage added successfully")


def update_topic(request, id):
    topic = Topic.objects.get(id=id)
    if request.method == "POST":
        new_name = request.POST.get("topic")
        topic = Topic.objects.filter(id=id).update(top_name=new_name)
    return render(request, "create_topic.html", {"topic": topic})


def update_webpage(request, id):
    if request.method == "POST":
        topic = request.POST.get("topic")
        name = request.POST.get("name")
        url = request.POST.get("url")
        # getting topic object address
        topic = Topic.objects.get(top_name=topic)
        webpage = Webpage.objects.filter(id=id).update(
            topic=topic, name=name, url=url)
    webpage = Webpage.objects.get(id=id)
    topics = Topic.objects.all()
    return render(request, "create_webpage.html", {"webpage": webpage, "topics": topics})
