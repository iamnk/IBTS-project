from django.shortcuts import render
from django.http import HttpResponse,Http404
from  .models import StudentEntry,Student
import datetime
# Create your views here.
def validation(request, reg_no):
    try:
        studentobj=Student.objects.get(roll_no=reg_no)
    except Student.DoesNotExist:
        #raise Http404("Invalid Register Number");
        return HttpResponse("Invalid")
    if studentobj.Fee == "paid":
        return HttpResponse("paid")
    else:
        travel_count=studentobj.studententry_set.count()
        if(travel_count<12):
            tdydate=datetime.date.today()
            entry=StudentEntry.objects.create(student=studentobj,date=tdydate)
            entry.save()
            return HttpResponse("%s"%(travel_count))
        else:
            return HttpResponse("Limit Exceeded")
