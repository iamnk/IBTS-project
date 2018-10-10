from django.shortcuts import render
from django.http import HttpResponse,Http404
from  .models import StudentEntry,Student
import datetime
# Create your views here.
def validation(request, rf_id):
    try:
        studentobj=Student.objects.get(rfvalue=rf_id)
    except Student.DoesNotExist:
        #raise Http404("Invalid Register Number");
        return HttpResponse("Invalid")
    if studentobj.Fee == "paid":
        return HttpResponse("WELCOME %s"%studentobj.roll_no)
    else:
        travel_count=11-studentobj.studententry_set.count()
        if(travel_count<12):
            tdydate=datetime.date.today()
            entry=StudentEntry.objects.create(student=studentobj,date=tdydate)
            entry.save()
            return HttpResponse("%s More"%(travel_count))
        else:
            return HttpResponse("Limit Exceeded")
