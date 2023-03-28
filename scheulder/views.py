from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .utils import CustomHTMLCal
from .models import Event
from .forms import EventForm, ServiceForm
from datetime import date
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)


class EventCreateView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = Event
    form_class = EventForm
    success_url = '/'
    def get_context_data(self, **kwargs): # dodaj więcej niz jeden formularz 
        context = super().get_context_data(**kwargs)
        context['event_form'] = EventForm()
        context['service_form'] = ServiceForm()
        return context
    def post(self, request, *args, **kwargs): #zapisz więcej niż jeden formularz 
        event_form = EventForm(request.POST)
        service = ServiceForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return redirect(('calendar:scheulder'))
        elif service.is_valid():
            service.save()
            return redirect(('calendar:add'))
    def get_success_message(self, cleaned_data):
        return f'Dodano - {self.object.service} | {self.object.date} | {self.object.time}'

        
        
class EventUpdateView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = Event
    form_class = EventForm
    template_name_suffix = '_update_form'
    success_url = '/'
    def get_initial(self):
        initial = super().get_initial()
        initial['date'] = self.object.date.strftime('%Y-%m-%d') # autouzupełnienie wymaga wskazania poprawnego formatowania daty oraz czasu dateinput wyświetlą sie w formacie yyyy/mm/dd
        initial['time'] = self.object.time.strftime('%H:%M')
        return initial
    def get_success_message(self, cleaned_data):
        return f'Zaktualizowano - {self.object.service} | {self.object.date} | {self.object.time}'
    

class EventDeleteView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model = Event
    success_url = '/'
    def get_success_message(self, cleaned_data):
        return f'Usunięto - {self.object.first_name} | {self.object.service} | {self.object.date} | {self.object.time}'
    

class EventDetailView(LoginRequiredMixin,DetailView):
    model = Event
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        data = {
            "pk" : obj.pk,
            "service": obj.service.service_name,
            "first_name": obj.first_name,
            "number": obj.number,
            "description": obj.description,
            "date": obj.date,
            "time": obj.time.strftime('%H:%M'),
            "paid": obj.paid,
        }
        return JsonResponse(data)

class CalendarView(ListView):
    model = Event
    template_name = 'scheulder/index.html'
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('/admin')
        return super(CalendarView, self).get(*args, **kwargs)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        
        d = get_date(self.request.GET.get('month', None))
        calendar = CustomHTMLCal(d.year,d.month)
        cal = calendar.formatmonth(d.year,d.month)
        
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context["cal"] = cal 
        return context

def get_date(req_day):
    if req_day:
        year = int(req_day.split('-')[0]) # Pobierz date z URL i rozdziel [0] parametr ROK
        month = int(req_day.split('-')[1]) # Pobierz date z URL i rozdziel [1] parametr MIESIĄc
        return date(year, month, day=1) # Zapisz w formie datetime
    return datetime.today() # Jeśli url jest pusty to zwraca dzisiejszą date
    

def prev_month(d):
    prev_month = d.month - 1
    if prev_month < 1: # Jeśli liczbą miesiąca spadnie poniżej 1 to ustaw miesiąc na 12
        next_month = 12 # Ustawia miesiąc na 1 (grudzień)
        next_year = d.year - 1 # Odejmuje rok -1
        next_year = datetime(next_year,next_month,1) # Konwertuje na grudzień z poprzednik rokiem
        return 'month=' + str(next_year.year) + '-' + str(next_month)
    
    month = datetime(d.year,prev_month, day=1) 
    return 'month=' + str(month.year) + '-' + str(month.month)



def next_month(d):
    next_month = d.month + 1 # Pobiera aktualny miesiac i dodaje +1 w typie INT
    if next_month > 12: # Jeśli liczbą miesiąca przekroczy 12 to dodaje +1 rok 
        next_month = 1 # Ustawia miesiąc na 1 (styczeń)
        next_year = d.year + 1 # Dodaje rok +1
        next_year = datetime(next_year,next_month,1) # konwertuje na styczeń z nastepnym rokiem
        return 'month=' + str(next_year.year) + '-' + str(next_month)
    
    next_month = datetime(d.year,next_month,1) # Zmieniamy next_month na datetime format i ustawiamy 
    return 'month=' + str(next_month.year) + '-' + str(next_month.month)
