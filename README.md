# so_question_47654662

How to use the reserved word "class" in Python for naming fields in Django and Django REST Framework

## Purpose

The purpose of this repo is to support my [question](https://stackoverflow.com/questions/47654662/django-rest-framework-doesnt-display-value-in-put-form) at StackOverflow.  
There is also another associated [question](https://stackoverflow.com/questions/47630356/using-the-reserved-word-class-as-field-name-in-django-and-django-rest-framewor).

## Introduction

Taxonomy is the science of defining and naming groups of biological organisms on the basis of shared characteristics. Organisms are grouped together into taxa (singular: taxon) and these groups are given a taxonomic rank. The principal ranks in modern use are domain, kingdom, phylum, class, order, family, genus and species.
More information on [Taxonomy](https://en.wikipedia.org/wiki/Taxonomy_(biology)) and [Taxonomic ranks](https://en.wikipedia.org/wiki/Taxonomic_rank) in Wikipedia.

## Goal

The goal is to create a JSON using Django REST Framework that will look like:

<pre></code>
{
    "canonical_name": "Red fox",
    "species": "Vulpes vulpes",
    "genus": "Vulpes",
    "family": "Canidae",
    "order": "Carnivora",
    <strong>"class": "Mammalia",</strong>
    "phylum": "Chordata",
    "kingdom": "Animalia",
    "domain": "Eukarya"
}
</code></pre>

The challenge is to achieve the result displayed in the bold line.

That can be solved by implementing the method `to_representation` in the serializer class. Since we can't name a model field `class`, we have to use another name, like `class_name`. In the method `to_representation` we intercept the data and replace `class_name` with `class`.  
However this helps only with read-only APIs. This solution prevents the PUT form of populating the input for `class_name`.

If you'd like to help me and get the bounty, please fork the repo and try to debug.

Using virtual environments for Python is strongly advised. You can install the dependencies with:

    pip install -r requirements.txt
    
Start the test server with:

    python manage.py runserver
    
and you should be ready to go.
