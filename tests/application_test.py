#1 : Import libraries need for the test
from application.models import Entry, User
import datetime as datetime
import pytest
from flask import json 


#2: Unit testing for users
#Unexpected unit testing
@pytest.mark.parametrize("userlist", [
    ( 'testuser', 'testpassword')
]) 
def test_user(userlist):
    user = User( username=userlist[0],password= userlist[1])
    assert user.username == userlist[0]
    assert user.password == userlist[1]

# Expected failure testing
#range testing
@pytest.mark.xfail
@pytest.mark.parametrize("userlist", [
    ('This_is_supposed_to_fail_due_to_the_fact_that_it_has_more_than_64_characters', 'testpassword'),

])
def testUserClass(userlist,capysys):
    test_user(userlist,capysys)



@pytest.mark.parametrize("name",[
    ["Username", "Password"]
])
def test_create_user(client,name,capsys):
    with capsys.disabled():
        # Prepare data into dictionary
        data = {
            "username": name[0],
            "password": name[1]
        }
        # use the client to post the data
        response = client.post('/api/user', data = json.dumps(data), content_type='application/json')
        response_body = json.loads(response.get_data(as_text=True))
        # check the response status code
        assert response.status_code == 200
        # check the response body
        assert response_body["id"]


#3: Get User
@pytest.mark.parametrize("id",[
    [1,"Username", "Password"]
])
def test_get_user(client,id,capsys):
    with capsys.disabled():
        # use the client to get the data
        response = client.get('/api/user/{}'.format(id[0]))
        response_body = json.loads(response.get_data(as_text=True))
        # check the response status code
        assert response.status_code == 200
        # check the response body
        assert response_body["id"] == id[0]
        assert response_body["username"] == id[1]
        assert response_body["password"] == id[2]


#Unit Test
#4: Parametrize section contains data for the test
@pytest.mark.parametrize("entrylist",[
    [1,0,1,0,1,0,1,0,1,0,1,1,40,200,30,"Testing",1,1]
])

#3: Test function
def test_entrylist(entrylist,capsys):
    with capsys.disabled():
        print(entrylist)
        now = datetime.datetime.now()
        new_entry = Entry(
            gender_male = entrylist[0],
            hypertension = entrylist[1],
            heartdisease = entrylist[2],
            married = entrylist[3],
            urban = entrylist[4],
            smoking = entrylist[5],
            smokeformerly = entrylist[6],
            govtjob = entrylist[7],
            workedbefore = entrylist[8],
            privatework = entrylist[9],
            selfemployed = entrylist[10],
            workchildren = entrylist[11],
            age = entrylist[12],
            average_glucose_level = entrylist[13],
            bmi = entrylist[14],
            name = entrylist[15],
            prediction = entrylist[16],
            user_id=entrylist[17],
            predicted_on = now
        )
        assert new_entry.user_id == entrylist[17]
        assert new_entry.gender_male == entrylist[0]
        assert new_entry.hypertension == entrylist[1]
        assert new_entry.heartdisease == entrylist[2]
        assert new_entry.married == entrylist[3]
        assert new_entry.urban == entrylist[4]
        assert new_entry.smoking == entrylist[5]
        assert new_entry.smokeformerly == entrylist[6]
        assert new_entry.govtjob == entrylist[7]
        assert new_entry.workedbefore == entrylist[8]
        assert new_entry.privatework == entrylist[9]
        assert new_entry.selfemployed == entrylist[10]
        assert new_entry.workchildren == entrylist[11]
        assert new_entry.age == entrylist[12]
        assert new_entry.average_glucose_level == entrylist[13]
        assert new_entry.bmi == entrylist[14]
        assert new_entry.name == entrylist[15]
        assert new_entry.prediction == entrylist[16]
        assert new_entry.predicted_on == now

    
#5: Expected failure testing
# what if input contains non-binary like 2,3
# what if prediction is negative
@pytest.mark.xfail(reason="arguments < 0")
@pytest.mark.parametrize("entrylist",[
    [-1,1,0,1,0,1,0,1,0,1,0,1,29,290.2,26,"TestingPut1",1,-1,-1],
    [1,-1,0,1,0,1,0,1,0,1,0,1,29,290.2,26,"TestingPut2",1,1-1],
    [1,1,-1,1,0,1,0,1,0,1,0,1,29,290.2,26,"TestingPut3",1,-2],
])
def test_EntryValidation(entrylist,capsys):
    test_entrylist(entrylist,capsys)

#6: Test add api
@pytest.mark.parametrize("entrylist",[
    [1,0,1,0,1,0,1,0,1,0,1,1,40,200,30,"Testing",1,1]
])
def test_addAPI(client,entrylist,capsys):
    with capsys.disabled():
        # prepare data in json
        data1 = {
            'user_id': entrylist[17],
            'gender_male': entrylist[0],
            'hypertension': entrylist[1],
            'heartdisease': entrylist[2],
            'married': entrylist[3],
            'urban': entrylist[4],
            'smoking': entrylist[5],
            'smokeformerly': entrylist[6],
            'govtjob': entrylist[7],
            'workedbefore': entrylist[8],
            'privatework': entrylist[9],
            'selfemployed': entrylist[10],
            'workchildren': entrylist[11],
            'age': entrylist[12],
            'average_glucose_level': entrylist[13],
            'bmi': entrylist[14],
            'name': entrylist[15],
            'prediction': entrylist[16],
        }
        # send post request
        response = client.post('/api/add', data=json.dumps(data1), content_type='application/json')
        # check response
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        response_body = json.loads(response.get_data(as_text=True))
        assert response_body['id']

#7: Test get api
@pytest.mark.parametrize("entrylist",[
    [1,0,1,0,1,0,1,0,1,0,1,1,40,200,30,"Testing",1,1,1]
])
def test_getAPI(client,entrylist,capsys):
    with capsys.disabled():
        response = client.get(f'/api/get/{entrylist[18]}')
        ret = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        response_body = json.loads(response.get_data(as_text=True))
        assert response_body['id'] == entrylist[18]
        assert response_body['user_id'] == entrylist[17]
        assert response_body['prediction'] == entrylist[16]
        assert response_body['name'] == entrylist[15]
        assert response_body["bmi"] == entrylist[14]
        assert response_body["average_glucose_level"] == entrylist[13]
        assert response_body["age"] == entrylist[12]
        assert response_body['workchildren'] == entrylist[11]
        assert response_body['selfemployed'] == entrylist[10]
        assert response_body['privatework'] == entrylist[9]
        assert response_body['workedbefore'] == entrylist[8]
        assert response_body['govtjob'] == entrylist[7]
        assert response_body['smokeformerly'] == entrylist[6]
        assert response_body['smoking'] == entrylist[5]
        assert response_body['urban']== entrylist[4]
        assert response_body['married'] == entrylist[3]
        assert response_body['heartdisease'] == entrylist[2]
        assert response_body['hypertension'] == entrylist[1]
        assert response_body['gender_male'] == entrylist[0]

#8: Test prediction api
@pytest.mark.parametrize("entrylist",[
    [1,0,1,0,1,0,1,0,1,0,1,1,40,200,30]
])
def test_predictionAPI(client,entrylist,capsys):
    with capsys.disabled():
        # prepare data in json
        data1 = {
            'gender_male': entrylist[0],
            'hypertension': entrylist[1],
            'heartdisease': entrylist[2],
            'married': entrylist[3],
            'urban': entrylist[4],
            'smoking': entrylist[5],
            'smokeformerly': entrylist[6],
            'govtjob': entrylist[7],
            'workedbefore': entrylist[8],
            'privatework': entrylist[9],
            'selfemployed': entrylist[10],
            'workchildren': entrylist[11],
            'age': entrylist[12],
            'average_glucose_level': entrylist[13],
            'bmi': entrylist[14]
        }
        response = client.post('/api/test/predict', data=json.dumps(data1), content_type='application/json')
        response_body = json.loads(response.get_data())
        assert response_body['prediction'] == "1" or response_body['prediction'] == "0"


#8 Test delete API
@pytest.mark.parametrize("entrylist",[
    [1,0,1,0,1,0,1,0,1,0,1,1,40,200,30,"Testing",1,1,1]
])
def test_deleteAPI(client,entrylist,capsys):
    with capsys.disabled():
        response = client.delete(f'/api/delete/{entrylist[18]}')
        ret = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        response_body = json.loads(response.get_data(as_text=True))
        # check outcome of result
        assert response_body['result']== 1

#9 Test Delete User API
@pytest.mark.parametrize("id",[
    1
])
def test_deleteUserAPI(client,id,capsys):
    with capsys.disabled():
        response = client.delete(f'/api/delete/user/{id}')
        ret = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json'
        response_body = json.loads(response.get_data(as_text=True))
        assert response_body['result'] == 1