from django.db import models
import json

ICONS = ['🎓','⚽','🏀','🏐','🎾','🥋','🤾','🚴','🧠','👔','🏫','📚','🏊','🏋️','🤸','⛹️','🎯','🏆']

class Guruh(models.Model):
    nom = models.CharField(max_length=200, verbose_name="Guruh nomi")
    rang = models.CharField(max_length=7, default='#00c6ff', verbose_name="Rang (hex)")
    ikonka = models.CharField(max_length=10, default='🎓', verbose_name="Ikonka")
    ikonka_rasm = models.ImageField(upload_to='ikonkalar/', blank=True, null=True, verbose_name="Ikonka rasmi (ixtiyoriy)")
    tartib = models.IntegerField(default=0, verbose_name="Tartib")
    yaratilgan = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['tartib', 'nom']
        verbose_name = "Guruh"
        verbose_name_plural = "Guruhlar"

    def __str__(self):
        return self.nom

    def get_lessons_by_week(self, week_monday):
        """week_monday: date object, returns dict {weekday: [lessons]}"""
        from datetime import timedelta
        result = {}
        for i in range(6):
            day = week_monday + timedelta(days=i)
            lessons = list(self.darslar.filter(sana=day).order_by('para'))
            result[day] = lessons
        return result

    def get_all_weeks(self):
        from datetime import timedelta
        dates = self.darslar.values_list('sana', flat=True).distinct().order_by('sana')
        weeks = []
        seen = set()
        for d in dates:
            monday = d - timedelta(days=d.weekday())
            if monday not in seen:
                seen.add(monday)
                weeks.append(monday)
        return weeks


class Dars(models.Model):
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE, related_name='darslar')
    sana = models.DateField(verbose_name="Sana")
    hafta_kuni = models.CharField(max_length=20, verbose_name="Hafta kuni")
    para = models.CharField(max_length=10, verbose_name="Para", blank=True)
    vaqt = models.CharField(max_length=20, verbose_name="Vaqt", blank=True)
    modul = models.TextField(verbose_name="Modul nomi")
    tur = models.CharField(max_length=50, verbose_name="Dars turi", blank=True)
    oqituvchi = models.CharField(max_length=200, verbose_name="O'qituvchi", blank=True)
    xona = models.CharField(max_length=50, verbose_name="Xona", blank=True)

    class Meta:
        ordering = ['sana', 'para']
        verbose_name = "Dars"
        verbose_name_plural = "Darslar"

    def __str__(self):
        return f"{self.guruh.nom} | {self.sana} | {self.modul[:30]}"

    @property
    def rang_class(self):
        """Return color class based on module number"""
        import re
        m = re.match(r'^(\d+)\.', self.modul.strip())
        if m:
            n = int(m.group(1))
            colors = ['mc-1','mc-2','mc-3','mc-4','mc-5']
            return colors[(n - 1) % len(colors)]
        return 'mc-0'

