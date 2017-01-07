 # encoding=utf-8
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from mywork.models import orashipping
from .forms  import v_orashipping  


def index(request):
    return HttpResponse(" You're at the mywork index.")

def create(request):
    queryset = orashipping.objects.all()


    context = {"title":'ahmed',
    "objects_list":queryset,

    }



    return render(request,"employee_form.html",context)




def detail(request):

    queryset = orashipping.objects.all()
    context = {"title":'ahmed',
    "objects_list":queryset,

    }

    return render(request,"detail.html",context)


			

def list(request):
    #instance= orashipping.objects.get(id=5)
    #instance= get_object_or_404(orashipping,type_no="1sa")
    form = v_orashipping()
    queryset = orashipping.objects.all()


    context = {"title":'ahmed',
    "objects_list":queryset,

    }
		

    return render(request,"index.html",context)



    #context)	
	







def update(request):
    return HttpResponse("<h1>update.</h1>")   


def delete(request):
    return HttpResponse("<h1>delete.</h1>")




def about(request):
    return HttpResponse("""<html><head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script type="text/javascript" src="/static/admin/js/vendor/jquery/jquery.min.js"></script>
        <script type="text/javascript" src="/static/admin/js/vendor/jquery/bootstrap.min.js"></script>
        <link href="/static/admin/css/font-awesome.min.css" rel="stylesheet" type="text/css">
        <link href="/static/admin/css/bootstrap.css" rel="stylesheet" type="text/css">
    </head><body>
        <div class="cover">
            <div class="navbar">
                <div class="container">
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-ex-collapse">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                        <a class="navbar-brand" href="#"><span>Brand</span></a>
                    </div>
                    <div class="collapse navbar-collapse" id="navbar-ex-collapse">
                        <ul class="nav navbar-nav navbar-right">
                            <li class="active">
                                <a href="#">Home</a>
                            </li>
                            <li>
                                <a href="#">Contacts</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="cover-image" style="background-image : url('https://unsplash.imgix.net/photo-1418479631014-8cbf89db3431?w=1024&amp;q=50&amp;fm=jpg&amp;s=478a9a2196033db7c0bf3c8ba3707f4d')"></div>
            <div class="container">
                <div class="row">
                    <div class="col-md-12 text-center">
                        <h1 class="text-inverse">Ahmed Alaa</h1>
                        <p class="text-inverse">dev python django.</p>
                        <br>
                        <br>
                        
                    </div>
                </div>
            </div>
        </div>
        
        
        <div class="section">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <h1 class="text-center text-primary">Ahmed</h1>
                        <p class="text-center">You Have Lot Of A Skills .</p>
                    </div>
                </div>
                
            </div>
        </div><div class="col-md-4 text-center">
                        <img class="center-block img-circle img-responsive" src="https://lh3.googleusercontent.com/-8T-S3-WgNww/Uzjgz3ABj7I/AAAAAAAAARY/2CfOWgGwKr0/BeFunky_null_17.jpg.jpg">
                        <h2 class="hidden-xs text-center">Ahmed Alaa Abd Alhy</h2>
                        <p class="text-center">Developer</p>
                    </div>
</body></html>""")





'''
	https://www.youtube.com/watch?v=zHd3RqxOBws&list=PLMYF6NkLrdN9JJ7r0APq7O87gucjYWRfD&index=31
C:\Users\Ahmed-pc\AppData\Local\pip\Cache\wheels\25\3d\4e\68e3245f66672da6b889d26e0dc3e943dc2457bd27483d2606
QuerySet
#queryset = orashipping.objects.all()
#   for obj in queryset:
#       print obj.objective#

#   form = orashipping
#   context = {
#           
#           "title":'ahmed',
#           "queryset":"queryset",
#           "form":form,
#           #

#               }   


             


#https://www.youtube.com/watch?v=9JbrwQApKpY

https://www.youtube.com/watch?v=KbOei4IRinc&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy&index=20


'''


