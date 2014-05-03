from django.db import models
from families.models import Family
from brands.models import Brand

# Create your models here.


class Equipment(models.Model):
	brand = models.ForeignKey(Brand)
	family = models.ForeignKey(Family)
	model = models.CharField(max_length = 255)
	specification = models.TextField()

	def __unicode__(self):
		return "%s -  %s" % (self.family, self.model)


	def get_absolute_url(self):
		return '/equipments/%s/' % self.model