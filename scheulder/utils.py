from calendar import HTMLCalendar
from .models import Event
from datetime import datetime
class CustomHTMLCal(HTMLCalendar):
    def __init__(self, year,month):
        self.year = year
        self.month = month
        super(CustomHTMLCal, self).__init__()
    
        
    def formatday(self, day: int, weekday: int) -> str:
        events = Event.objects.filter(date__day=day) # Pobiera elementy i sortuje po dniach date__day (określa filtrowanie po dniach) = day (wskazuje bezpośrednio o który dzien chodzi)
        event = ''
        for i in events:
            if i.date.month == self.month and i.date.year == self.year: 
                if i.paid:
                    event += "<li><a class='d-flex justify-content-center btn btn-success btn-sm' data-bs-toggle='modal' data-bs-target='.modal' id='modal-btn' href='#' data-url='{}'><div class='service-name'>{}</div> <div class='service-time'>{}</div></a></li>".format(i.get_absolute_url(),i.service,i.time.strftime("%H:%M")) 
                else:
                    event += "<li><a class='d-flex justify-content-center btn btn-danger btn-sm' data-bs-toggle='modal' data-bs-target='.modal' id='modal-btn' href='#' data-url='{}'><div class='service-name'>{}</div> <div class='service-time'>{}</div></a></li>".format(i.get_absolute_url(),i.service,i.time.strftime("%H:%M"))
        if day == 0:
            return '<td><div class="noday">&nbsp;</div></td>' # dni poza miesiącem
        else:

            return f'<td ><div class="{self.cssclasses[weekday]} day"><p>{day}</p><ul class="readmore">{event}</ul></div></td>'

    def formatmonthname(self, theyear: int, themonth: int, withyear):
        month = datetime(theyear, themonth,1)
        months = {
            1:'Styczeń',
            2:'Luty',
            3:'Marzec',
            4:'Kwiecień',
            5:'Maj',
            6:'Czerwiec',
            7:'Lipiec',
            8:'Sierpień',
            9:'Wrzesień',
            10:'Październik',
            11:'Listopad',
            12:'Grudzień',
        }
        return f"<tr><th class='text-center month-head h1' colspan='7'>{months[month.month]} {month.strftime('%Y')}</th></tr>"



    def formatweekheader(self) -> str:
        days = ['Poniedziałek','Wtorek','Środa','Czwartek','Piątek','Sobota','Niedziela']
        day = ''
        for i in days:
            day += f"<th class='weekday'>{i}</th>"
        return day

    cssclasses = [style + " text-nowrap" for style in
                  HTMLCalendar.cssclasses]
    cssclass_month_head = "text-center month-head h2"
    cssclass_month = "text-center month"
    cssclass_year = "text-italic lead"