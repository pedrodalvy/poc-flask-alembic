from http import HTTPStatus

from src.models.user import User


def test_should_list_users(client, session):
    # Arrange
    user1 = User(email='john@email.com')
    user2 = User(email='jane@email.com')
    session.add_all([user1, user2])
    session.commit()

    # Act
    response = client.get('/users/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert len(response.json) == 2
    assert response.json[0]['email'] == 'john@email.com'
    assert response.json[1]['email'] == 'jane@email.com'


def test_should_get_user_by_id(client, session):
    # Arrange
    user = User(email='john@email.com')
    session.add(user)
    session.commit()

    # Act
    response = client.get(f'/users/{user.id}')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json['email'] == 'john@email.com'


def test_should_return_404_when_user_not_found(client, session):
    # Arrange
    non_existent_id = 999

    # Act
    response = client.get(f'/users/{non_existent_id}')

    # Assert
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_should_create_user(client, session):
    # Arrange
    user_data = {
        'email': 'john@email.com'
    }

    # Act
    response = client.post('/users/', json=user_data)

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json['email'] == user_data['email']

    # Verify user was actually created in the database
    created_user = session.query(User).first()
    assert created_user is not None
    assert created_user.email == user_data['email']
