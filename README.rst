.. _main_page:

PyWOT: World of Tanks API для Python 
========================================

.. begin_description

.. image:: https://travis-ci.org/mattselph/pywot.svg?branch=master
		   :target: https://travis-ci.org/mattselph/pywot

Это интерфейс World of Tanks API для Python .  
Чтобы работать с API вы должны авторизоваться на `Wargaming.net <https://na.wargaming.net/developers>`_
и получить ID приложения. 
Все получаемые данные в формате JSON

.. end_description

.. begin_installation:

Установка
------------

На данный момент, PyWOT работает на Python 2.6, 2.7.  Пакет легко ставится через pip:

.. code-block:: bash

	$ pip install pywot

.. end_installation

.. begin_usage

Как это работает
-----

Подключаем API и указываем ID. Всё.
Код ниже получит список всех танков в игре :

.. code-block:: pycon

	>>> from pywot.api import API
	>>> from pywot.tankopedia import Tankopedia
	>>> app = API('your-app-id')
	>>> t = Tankopedia(app.app_id)
	>>> print t.list_of_vehicles()

Получить подробную информацию о конкретном танке можно через метод *vehicle_details* . 
Вот так мы узнаем всё о Квасе:

.. code-block:: pycon
	
	>>> print t.vehicle_details(tank_id=18689)

Или получить лишь несколько полей:

.. code-block:: pycon

	>>> print t.vehicle_details(
		tank_id=18689, 
		fields=['tank_id', 'nation', 'speed_limit', 'engines.module_id'])

Имена полей могут быть получены из `API Reference <https://na.wargaming.net/developers/api_reference/wot/account/list>`_.
Поиск можно вести по нескольким объектам, передав ключи в виде списка строк.

.. code-block:: pycon

	>>> print t.vehicle_details(
		tank_id=['18689','33'], 
		fields=['tank_id', 'nation', 'speed_limit', 'engines.module_id'])

PyWOT поддерживает несколько языков:

.. code-block:: pycon

	>>> print t.vehicle_details(
		language='ko', 
		tank_id=['18689','33'], 
		fields=['tank_id', 'nation', 'speed_limit', 'engines.module_id'])
Чтобы увидеть доступную статистику игрока, сначала ищем его через *search_players*.
Если у вас есть точный ник игрока , используйте get_account_id для получения account_id этого игрока.
Чтобы получить все достижения игрока с ником " lulz_man " делаем следующее:

.. code-block:: pycon

	>>> from pywot.api import API
	>>> from pywot.player import Player
	>>> app = API('your-app-id')
	>>> p = Player(app.app_id)
	>>> print p.player_achievements(account_id=p.get_account_id(nickname='lulz_man'))

.. end_usage

.. begin_license

License
-------

All of the code contained here is licensed by
`the Apache 2.0 License <https://github.com/mattselph/pywot/blob/master/LICENSE>`_.

.. end_license
