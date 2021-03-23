## Home Automation using Python/Django 

Back end API for a Home Automation System built using Django REST Framework.

### Getting Started

Setup project environment with venv and pip.

```sh
$ python -m venv venv
$ venv/Scripts/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

### Libraries

These are the libraries that are used in this project.
requirements.txt should have the following lines:

```
asgiref==3.3.1
atomicwrites==1.4.0
attrs==20.3.0
autopep8==1.5.6
certifi==2020.12.5
chardet==4.0.0
colorama==0.4.4
coreapi==2.3.3
coreschema==0.0.4
Django==3.1.7
djangorestframework==3.12.2
idna==2.10
iniconfig==1.1.1
itypes==1.2.0
Jinja2==2.11.3
MarkupSafe==1.1.1
packaging==20.9
pluggy==0.13.1
psycopg2==2.8.6
py==1.10.0
pycodestyle==2.7.0
pyparsing==2.4.7
pytest==6.2.2
pytest-django==4.1.0
pytz==2021.1
requests==2.25.1
sqlparse==0.4.1
toml==0.10.2
uritemplate==3.0.1
urllib3==1.26.4
```
### API Documentation - Blog API

Use this route to get route description

```
route: /docs/
ie. http://127.0.0.1:8000/docs/
```

### Routes

- This routes provides information related to different objects.
- Anyone can retrieve th eobjects by sending `GET` request.
- Only Admin can modify the objects by sending `POST`,`PUT`,`PATCH`
and `DELETE` requests.

```
$ /api/
- List all home objects including room and lights objects 

$ /api/rooms
- List all room objects including lights objects 

$ /api/lights
- List all lights objects

$ /api/<home_id>/
- Retrieve a perticular home object 

$ /api/<home_id>/<room_id>/
- Retrieve a perticular room object of a perticular home object

$ /api/<home_id>/<room_id>/<light_id>/
- Retrieve a perticular light object of a room object of a perticular home object

$ /api/loglights
- Retrieve logs for changing a status of lights

$ /api/logthermostat
- Retrieve logs for changing a mode of thermostat

$ /api/logroomtemp
- Retrieve logs for changing a value of temperature of a room
```

### API Testing - pytest

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

### Fetures

- API keep track of changes made on home, room or light object such as
log entry for thermostat mode change, log entry for room temperature change,
log entry for status change for room lights.
- One endpoint to get all the data objects

### Coding Convention

- Pep8 coding style

### Future Modifications

- Create Owner for the individual home objects and
give additional permission to owners to modify the home objects. 
- API optimization to achieve:
    - Speed up in response times
    - Number of lines of code
    - Number of function calls
    - Allocated memory