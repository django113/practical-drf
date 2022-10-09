from datetime import datetime

from django.db.models import F, Min, Q
from django.shortcuts import render

# Create your views here.
from blog.models import Blog, Entry, Author

# ============================
# 1.Creating objects
# ============================
"""
create new item

To create and save an object in a single step, use the create() method.

"""
b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
b.save()  # Django doesn’t hit the database until you explicitly call save().

"""
update the objects?

Django doesn’t hit the database until you explicitly call save().
"""
b.name = "new name"
b.save()

"""
Saving ForeignKey and ManyToManyField fields
1.Updating a ForeignKey field works exactly the same way as saving a normal field

"""

entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name="Cheddar Talk")
entry.blog = cheese_blog
entry.save()

"""
2.many to many field updated 

Updating a ManyToManyField works a little differently – use the add() 
method on the field to add a record to the relation. 
adds the Author instance joe to the entry object:
"""

joe = Author.objects.create(name="Joe")
entry.authors.add(joe)

# ============================
# 2.Retrieving objects
# ============================

# Retrieving all objects
all_entries = Entry.objects.all()
# Retrieving specific objects with filters¶
# filter(**kwargs)
# exmples:
Entry.objects.filter(pub_date__year=2006)
Entry.objects.all().filter(pub_date__year=2006)

# exclude(**kwargs)


# Chaining filters using:
# ============================
Entry.objects.filter(
    headline__startswith='What'
).exclude(
    pub_date__gte=datetime.date.today()
).filter(
    pub_date__gte=datetime.date(2005, 1, 30)
)

# Filtered QuerySets are unique

q1 = Entry.objects.filter(headline__startswith="What")
q2 = q1.exclude(pub_date__gte=datetime.date.today())
q3 = q1.filter(pub_date__gte=datetime.date.today())

# ===================================================
# querie set is lazy
# ===================================================
q = Entry.objects.filter(headline__startswith="What")
q = q.filter(pub_date__lte=datetime.date.today())
q = q.exclude(body_text__icontains="food")
print(q)

# ======================================================
"""
Retrieving a single object with get()
you can use the get() method on a Manager which 
returns the object directly:

Note that there is a difference between using get(), and using filter() 
with a slice of [0]. If there are no results 
that match the query, get() will raise a DoesNotExist exception. 
"""
one_entry = Entry.objects.get(pk=1)

# ======================================================
"""
Other QuerySet methods

Most of the time you’ll use all(), get(), filter() and exclude()

"""

# ======================================================


"""
Limiting QuerySets:

"""
Entry.objects.all()[:5]
Entry.objects.all()[5:10]
Entry.objects.all()[:10:2]
Entry.objects.order_by('headline')[0:1].get()  # DoesNotExist not existing error

Blog.objects.filter(entry__authors__isnull=False, entry__authors__name__isnull=True)
Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)

# ======================================================
from datetime import date

pop = Blog.objects.create(name='Pop Music Blog')

Entry.objects.create(
    blog=pop,
    headline='Lennon Would Have Loved Hip Hop',
    pub_date=date(2020, 4, 1),
)

# ======================================================

"""
For date and date/time fields, you can add or subtract a timedelta object
more than 3 days after they were published:
"""
from datetime import timedelta

Entry.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))
# ======================================================


"""
For example, to find a list of all blog entries that have had more 
comments than pingbacks, we construct an 
F() object to reference the pingback count, and use that
F() object in the query:
"""
Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))

Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks') * 2)

# the rating of the entry is less than the sum of the
# pingback count and comment count
Entry.objects.filter(rating__lt=F('number_of_comments') + F('number_of_pingbacks'))

"""
An F() object with a double underscore will 
introduce any joins needed to access the related object
"""

Entry.objects.filter(authors__name=F('blog__name'))

Entry.objects.filter(pub_date__year=F('mod_date__year'))

Entry.objects.aggregate(first_published_year=Min('pub_date__year'))

# ======================================================
"""
This example finds the value of the highest rated entry and the total 
number of comments on all entries for each year:
>>> from django.db.models import OuterRef, Subquery, Sum
>>> Entry.objects.values('pub_date__year').annotate(
...     top_rating=Subquery(
...         Entry.objects.filter(
...             pub_date__year=OuterRef('pub_date__year'),
...         ).order_by('-rating').values('rating')[:1]
...     ),
...     total_comments=Sum('number_of_comments'),
... )
"""
# ======================================================


# The pk lookup shortcut
# ========================
Blog.objects.get(id__exact=14)  # Explicit form
Blog.objects.get(id=14)  # __exact is implied
Blog.objects.get(pk=14)  # pk implies id__exact
# ======================================================


"""
Caching and QuerySets
"""

queryset = Entry.objects.all()
print([p.headline for p in queryset])  # Evaluate the query set.
print([p.pub_date for p in queryset])  # Reuse the cache from the evaluation.

# ======================================================


# ========================Asynchronous queries=====================

"""
1.aget() or adelete()
2.async for entry in Authors.objects.filter(name__startswith="A"):



user = await User.objects.filter(username=my_input).afirst()

"""

Q(question__startswith='Who') | Q(question__startswith='What')

# ========================Asynchronous queries=====================



"""
# ========================Asynchronous queries=====================
Comparing objects
"""
some_entry == other_entry
some_entry.id == other_entry.id



"""
Deleting objects
"""
Entry.objects.filter(pub_date__year=2005).delete()
# e.delete()
"""
After duplicating an entry, 
you must set the many-to-many relations for the new entry:
"""
entry = Entry.objects.all()[0] # some previous entry
old_authors = entry.authors.all()
entry.pk = None
entry._state.adding = True
entry.save()
entry.authors.set(old_authors)


"""
OneToOneFieldusing for this
"""

# detail = EntryDetail.objects.all()[0]
# detail.pk = None
# detail._state.adding = True
# detail.entry = entry
# detail.save()


"""
Updating multiple objects at once
"""
b = Blog.objects.get(pk=1)

# Change every Entry so that it belongs to this Blog.
Entry.objects.update(blog=b)
# Update all the headlines belonging to this Blog.
Entry.objects.filter(blog=b).update(headline='Everything is the same')
Entry.objects.update(number_of_pingbacks=F('number_of_pingbacks') + 1)
Entry.objects.update(headline=F('blog__name'))
Entry.objects.update(number_of_pingbacks=F('number_of_pingbacks') + 1)



for item in my_queryset:
    item.save()





