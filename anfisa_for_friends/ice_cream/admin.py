from django.contrib import admin

# Register your models here.

# Из модуля models импортируем модель Category...
from .models import Category, Topping, Wrapper, IceCream

# Создаём класс, в котором будем описывать настройки админки:

admin.site.empty_value_display = 'Не задано'


class IceCreamAdmin(admin.ModelAdmin):
    # В этом классе опишем все настройки, какие захотим.
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',

    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)
# какие поля будут показаны на странице списка объектов (свойство list_display,
#  это кортеж); какие поля можно редактировать прямо на странице
#  списка объектов (свойство list_editable, кортеж);search_fields — кортеж
#  с перечнем полей, по которым будет проводиться поиск. Форма
#  поиска отображается над списком элементов.list_filter — кортеж
#  с полями, по которым можно фильтровать записи. Фильтры
#  отобразятся справа от списка элементов.В кортеже
# list_display_links указывают поля, при клике на которые можно
#  перейти на страницу просмотра и редактирования записи.
#  По умолчанию такой ссылкой служит первое отображаемое поле.
# Это свойство сработает для всех полей этой модели.
# Вместо пустого значения будет выводиться строка "Не задано".
#    empty_value_display = 'Не задано'

# Изменим интерфейс так, чтобы связанные записи можно было перекладывать
# из одного окошка в другое.
    filter_horizontal = ('toppings',)


# На страницу редактирования категории можно подгрузить блок с информацией
# о связанных с ней сортах мороженого.
# Такие блоки называют «вставки», для их настройки в Django есть классы
#  admin.TabularInline и admin.StackedInline. Разница между этими
# классами заключается лишь в способе отображения связанных записей:
#  TabularInline отображает поля вставки в строку, а StackedInline
#  — столбцом, одно под другим.

# Подготавливаем модель IceCream для вставки на страницу другой модели.
# class IceCreamInline(admin.StackedInline):
class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


# Переопределяем Category на CategoryAdmin
admin.site.register(Category, CategoryAdmin)
# Регистрируем новый класс:
# указываем, что для отображения админки модели IceCream
# вместо стандартного класса нужно использовать класс IceCreamAdmin
admin.site.register(IceCream, IceCreamAdmin)

# ...и регистрируем её в админке:
# admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(Wrapper)
# admin.site.register(IceCream)

# Этот вариант сработает для всех моделей приложения.
# Вместо пустого значения в админке будет отображена строка "Не задано".
# admin.site.empty_value_display = 'Не задано'
