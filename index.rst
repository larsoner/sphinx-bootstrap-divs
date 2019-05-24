<div> helpers for sphinx-bootstrap-theme
========================================

Installation
------------

.. code-block:: console

    $ pip install sphinx-bootstrap-divs

Code
----
::

    .. collapse:: Open by default
       :open:

       But closes when you click on it.

    .. collapse:: Closed by default
       :class: info

       But opens when you click on it.

    .. details:: Closed by default

       But opens when you click on it.

Output
------

.. collapse:: |folder-open-o| Open by default
   :open:

   But |folder-o| closes when you click on it.

.. collapse:: |folder-o| Closed by default
   :class: info

   But |folder-open-o| opens when you click on it.

.. details:: |folder-o| Closed by default

   But |folder-open-o| opens when you click on it.
