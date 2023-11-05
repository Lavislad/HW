from django.contrib import admin
from django.db import models
from django.utils.html import format_html
#Таблица 1
class Advertisement(models.Model):
    # 1-е в скобках - подсказка
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_length=10, decimal_places=2, max_digits=20)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id{self.id}, title={self.title}, price={self.price: .2f})>'

    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description="Дата обновления")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: orange; font-weight: bold;">Сегодня в {}</span>', updated_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')