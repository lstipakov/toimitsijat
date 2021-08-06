from django.db import models
from django.utils.translation import ugettext_lazy as _
import logging
import random

logger = logging.getLogger(__name__)

class Task(models.Model):
    class Meta:
        verbose_name = _("Toimitsijatehtävä")
        verbose_name_plural = _("Toimitsijatehtävät")

    TASK_TYPE_CHOICES = [
        ('Kello', 'Kello'),
        ('Kuulutus', 'Kuulutus'),
        ('Jäähy', 'Jäähy'),
        ('Pöytäkirja', 'Pöytäkirja'),
        ('Titu', 'Titu'),
        ('Kuvaaja', 'Kuvaaja'),
    ]
    
    task_type = models.CharField(
        choices=TASK_TYPE_CHOICES,
        default='Jäähy',
        max_length=64,
        unique=True
    )

    def __str__(self):
        return "%s" % (self.task_type)

    def parents(self):
        return [p for p in self.parent_set.all()]

class Parent(models.Model):
    class Meta:
        verbose_name = _("Vanhempi")
        verbose_name_plural = _("Vanhemmat")

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_tasks(self):
        return [t for t in self.tasks.all()]
    get_tasks.short_description = "Toimitsijatehtävät"

    def children(self):
        return [c for c in self.child_set.all()]
    children.short_description = "Pelaajat"

class Child(models.Model):
    class Meta:
        verbose_name = _("Pelaaja")
        verbose_name_plural = _("Pelaajat")
        
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    parents = models.ManyToManyField(Parent, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_parents(self):
        return [p for p in self.parents.all()]

class Arena(models.Model):
    class Meta:
        verbose_name = _("Pelikenttä")
        verbose_name_plural = _("Pelikentät")

    name = models.CharField(max_length=64)

    def __str__(self):
        return "%s" % (self.name)

class Match(models.Model):
    class Meta:
        verbose_name = _("Peli")
        verbose_name_plural = _("Pelit")

    date = models.DateField()
    place = models.ForeignKey(Arena, on_delete=models.CASCADE)
    opponent = models.CharField(max_length=64)
    players = models.ManyToManyField(Child)

    kello = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True, related_name="related_kello")
    kuulutus = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True, related_name="related_kuulutus")
    jäähy_1 = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True, related_name="related_jäähy_1")
    jäähy_2 = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True, related_name="related_jäähy_2")
    pöytäkirja = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True, related_name="related_pöytäkirja")
    titu = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True, related_name="related_titu")
    kuvaaja = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True, related_name="related_kuvaaja")

    def __str__(self):
        return "%s, vastaassa %s" % (self.place, self.opponent)

    def get_toimitsija(self, parents, exclude):
        p = [p for p in parents if p not in exclude]
        return random.choice(p) if p else None

    def luo_toimitsijalista(self):
        parents = []
        for p in self.players.all():
            parents.extend(p.parents.all())        
        
        chosen_parents = {}
        for t in Task.TASK_TYPE_CHOICES:
            chosen_parents[t[0]] = []
            for p in parents:                
                if (p.tasks.filter(task_type=t[0]).first()):
                    chosen_parents[t[0]].append(p)                
                
        self.kello = self.get_toimitsija(chosen_parents["Kello"], [])
        self.kuulutus = self.get_toimitsija(chosen_parents["Kuulutus"], [self.kello])
        self.jäähy_1 = self.get_toimitsija(chosen_parents["Jäähy"], [self.kello, self.kuulutus])
        self.jäähy_2 = self.get_toimitsija(chosen_parents["Jäähy"], [self.kello, self.kuulutus, self.jäähy_1])
        self.pöytäkirja = self.get_toimitsija(chosen_parents["Pöytäkirja"], [self.kello, self.kuulutus, self.jäähy_1, self.jäähy_2])
        self.titu = self.get_toimitsija(chosen_parents["Titu"], [self.kello, self.kuulutus, self.jäähy_1, self.jäähy_2, self.pöytäkirja])
        self.kuvaaja = self.get_toimitsija(chosen_parents["Kuvaaja"], [self.kello, self.kuulutus, self.jäähy_1, self.jäähy_2, self.pöytäkirja, self.titu])
