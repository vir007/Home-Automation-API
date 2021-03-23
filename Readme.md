### Home Automation using Python/Django 

Home Automation Rest API built using Django REST Framework.

## Getting Started

Setup project environment with venv and pip.

```sh
$ python -m venv venv
$ venv/Scripts/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

## Libraries

These are the libraries that are used in this project.
requirements.txt should have the following lines:

```
asgiref==3.3.1
atomicwrites==1.4.0
attrs==20.3.0
colorama==0.4.4
Django==3.1.7
djangorestframework==3.12.2
iniconfig==1.1.1
packaging==20.9
pluggy==0.13.1
psycopg2==2.8.6
py==1.10.0
pyparsing==2.4.7
pytest==6.2.2
pytest-django==4.1.0
pytz==2021.1
sqlparse==0.4.1
toml==0.10.2
```

## API Testing - pytest

All Testcases are covered and tested using pytest library.
Write this one line command to test the whole API.
```
$ pytest -v

tests/home_api/test_home_views.py::TestHomeListAnonymous::test_anyone_can_get_home_list PASSED                                                               [  5%] 
tests/home_api/test_home_views.py::TestHomeListAdmin::test_only_admin_can_post_new_home PASSED                                                               [ 11%] 
tests/home_api/test_home_views.py::TestHomeDetailAnonymous::test_anyone_can_get_home_detail PASSED                                                           [ 16%] 
tests/home_api/test_home_views.py::TestHomeDetailAdmin::test_only_admin_can_delete_a_home PASSED                                                             [ 22%] 
tests/home_api/test_home_views.py::TestHomeDetailAdmin::test_only_admin_can_patch_a_home PASSED                                                              [ 27%] 
tests/home_api/test_home_views.py::TestHomeDetailAdmin::test_only_admin_can_update_a_home PASSED                                                             [ 33%] 
tests/home_api/test_lights_views.py::TestLights::test_anyone_can_get_lights_list PASSED                                                                      [ 38%]
tests/home_api/test_lights_views.py::TestLightsListAdmin::test_only_admin_can_post_new_light PASSED                                                          [ 44%]
tests/home_api/test_lights_views.py::TestLightsDetailAnonymous::test_anyone_can_get_light_detail PASSED                                                      [ 50%]
tests/home_api/test_lights_views.py::TestRoomDetailAdmin::test_only_admin_can_delete_a_light PASSED                                                          [ 55%]
tests/home_api/test_lights_views.py::TestRoomDetailAdmin::test_only_admin_can_patch_a_light PASSED                                                           [ 61%]
tests/home_api/test_lights_views.py::TestRoomDetailAdmin::test_only_admin_can_update_a_light PASSED                                                          [ 66%]
tests/home_api/test_room_views.py::TestRooms::test_anyone_can_get_rooms_list PASSED                                                                          [ 72%]
tests/home_api/test_room_views.py::TestRoomListAdmin::test_only_admin_can_post_new_room PASSED                                                               [ 77%]
tests/home_api/test_room_views.py::TestRoomDetailAnonymous::test_anyone_can_get_room_detail PASSED                                                           [ 83%]
tests/home_api/test_room_views.py::TestRoomDetailAdmin::test_only_admin_can_delete_a_room PASSED                                                             [ 88%]
tests/home_api/test_room_views.py::TestRoomDetailAdmin::test_only_admin_can_patch_a_room PASSED                                                              [ 94%]
tests/home_api/test_room_views.py::TestRoomDetailAdmin::test_only_admin_can_update_a_room PASSED                                                             [100%]

======================================================================= 18 passed in 7.31s ========================================================================
```


## API Documentation - Blog API

Use this route to get route description

```
route: /docs/
ie. http://127.0.0.1:8000/docs/

```

## Fetures

- API keep track of changes made on home, room or light object such as
log entry for thermostat mode change, log entry for room temperature change,
log entry for status change for room lights.

## Coding Convention

- Pep8 coding style