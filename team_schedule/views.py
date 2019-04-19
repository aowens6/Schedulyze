from django.shortcuts import render

def home(request):
    return render(request, 'team_schedule/teamSchedule.html')
