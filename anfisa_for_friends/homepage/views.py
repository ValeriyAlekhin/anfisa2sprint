# homepage/views.py
# import datetime
from django.shortcuts import render
from ice_cream.models import IceCream
from django.db.models import Q


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
    ).filter(
        # Делаем запрос, объединяя два условия
        # через Q-объекты и оператор AND:
        Q(is_published=True) & Q(is_on_main=True)
        # order_by ограничиваем на главной странице не более 3 записей
    ).order_by('title')[1:4]
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)

# Значение оператора	SQL	       ORM
# Равно	                 =	    __exact
# Сравнение с NULL	  IS NULL 	__exact=None
# Больше	                 >	    __gt
# Больше или равно	     >=	    __gte
# Меньше	                 <	    __lt
# Меньше или равно	     <=	    __lte
# Поиск по тексту	LIKE '%фраза%'	__contains='фраза'
# Вхождение в множество	IN (1, 3, 4)	__in=[1, 3, 4]
# Вхождение в диапазон	BETWEEN 1 AND 4	__range=[1, 4]

# Предположим, в каком-нибудь проекте блога есть модель Pоst (публикация)
# и одно из полей этой модели — дата публикации.

# def filtered_date(request):

#    start_date = datetime.date(1890, 1, 1)
#    end_date = datetime.date(1895, 3, 31)
#    Post.objects.filter(pub_date__range=(start_date, end_date))
    # SQL-версия запроса: WHERE pub_date BETWEEN '1890-01-01' AND '1895-03-31';
#    return render(request, template_name, context)

# Для таких запросов в Django ORM применяют дополнительные суффиксы __date,
# __year, __month, __day, __week, __week_day, __quarter:
# Условия для конкретной даты:
# Post.objects.filter(pub_date__date=datetime.date(1890, 1, 1))
# Ранее первого января 1895 года:
# Post.objects.filter(pub_date__date__lt=datetime.date(1895, 1, 1))
# В конкретный год:
# Post.objects.filter(pub_date__year=1890)
# В любой год с января по июнь включительно:
# Post.objects.filter(pub_date__month__lte=6)
# В первый квартал любого года:
# Post.objects.filter(pub_date__quarter=1)
