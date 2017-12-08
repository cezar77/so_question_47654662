from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify


class Species(models.Model):
    canonical_name = models.CharField(
        max_length=50,
        unique=True,
        db_index=True
    )
    slug = models.SlugField(max_length=50)
    species = models.CharField(max_length=30)
    genus = models.CharField(max_length=30)
    subfamily = models.CharField(max_length=30, blank=True)
    family = models.CharField(max_length=30)
    order = models.CharField(max_length=30)
    class_name = models.CharField('Class', db_column='class', max_length=30)
    phylum = models.CharField(max_length=30)
    ncbi_id = models.PositiveSmallIntegerField('NCBI ID', unique=True)

    class Meta:
        verbose_name = 'Species'
        verbose_name_plural = 'Species'
        ordering = ('species',)

    def __str__(self):
        return '{} ({})'.format(self.canonical_name, self.species)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self)
        super(Species, self).save(*args, **kwargs)

    @cached_property
    def ncbi_taxonomy(self):
        url = 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={}'
        return url.format(self.ncbi_id)
