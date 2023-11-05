from django.db import models
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
