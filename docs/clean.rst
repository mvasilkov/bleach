==================
``bleach.clean()``
==================

``clean()`` is Bleach's HTML sanitization method:

.. code-block: python

    def clean(text, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES,
              styles=ALLOWED_STYLES, strip=False, strip_comments=True):
        """Clean an HTML fragment and return it."""
