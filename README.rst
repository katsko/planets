=======
Planets
=======

API-server: Python, Flask and `Apium <https://github.com/katsko/apium>`_.

This is `jsonrpc-server <https://www.jsonrpc.org/specification>`_  with two simple APIs.


API methods
===========

get_planets
-----------

Description
~~~~~~~~~~~

Return list of planets: names and distances.

List can be filter by *distance* parameter and sorted by *order* parameter.

Parameters
~~~~~~~~~~

* *distance* - int, optional
* *order* - str, optional, default: 'distance'; values: 'name' or 'distance'

Answer
~~~~~~

* *planets* - list(obj):
  * *name* - str
  * *distance* - int

CURL request
~~~~~~~~~~~~

.. code-block:: shell-session

    curl -X POST -d '{"jsonrpc": "2.0", "method": "get_planets", "params": {"order": "name", "distance": 778330257}, "id": "uuid-123"}' -H 'Content-Type: application/json' http://localhost:10800/api/

Browser js-console request
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   fetch("http://localhost:10800/api/", {method: 'POST', body: '{"jsonrpc":"2.0", "method": "get_planets", "params":{"order": "name", "distance": 778330257}, "id": "uuid-123"}'}).then((response) => {return response.json();}).then((data) => {console.log(data);});



get_planet
----------

Description
~~~~~~~~~~~

Return one planet by *name* parameter.

Parameters
~~~~~~~~~~

* *name* - str

Answer
~~~~~~

* *planet* - obj:
  * *name* - str
  * *distance* - int
  * *planet_type* - str

CURL request
~~~~~~~~~~~~

.. code-block:: shell-session

    curl -X POST -d '{"jsonrpc": "2.0", "method": "get_planet", "params": {"name": "Earth"}, "id": "uuid-456"}' -H 'Content-Type: application/json' http://localhost:10800/api/

Browser js-console request
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   fetch("http://localhost:10800/api/", {method: 'POST', body: '{"jsonrpc":"2.0", "method": "get_planet", "params":{"name": "Earth"}, "id": "uuid-456"}'}).then((response) => {return response.json();}).then((data) => {console.log(data);});


For backenders
==============

Requirements
------------

Python 3.8+

Install
-------

.. code-block:: shell-session

   git clone https://github.com/katsko/planets.git
   python -m venv planets_venv
   source planets_venv/bin/activate
   cd planets
   pip install -r requires.txt

Run server
----------

.. code-block:: shell-session

   cd planets
   ./main_flask.py  # http://localhost:10800/
