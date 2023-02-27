Usage
=====

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install demo-precommit

Example Recipe
--------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. py:function:: lumache.get_random_ingredients(kind=None)

   Return a list of random ingredients as strings.

   :param kind: Optional "kind" of ingredients.
   :type kind: list[str] or None
   :raise lumache.InvalidKindError: If the kind is invalid.
   :return: The ingredients list.
   :rtype: list[str]

.. py:exception:: lumache.InvalidKindError

   Raised if the kind is invalid.
