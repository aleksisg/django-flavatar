django-flavatar
===============

Create Flavatars (First Letter Avatars - just like what Google does in GMail) in Django templates. The code creates a box with the first letter of the variable in the middle and gives it a background colour based on a hash of the variable.

Just put it in your templatetags directory and then call it in your templates with {% load flavatar %} and then {{ variable|flavatar }}
