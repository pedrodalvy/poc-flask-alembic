import pytest
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from src.app import create_app
from src.models.base import Base, db


@pytest.fixture(scope='function')
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })

    with app.app_context():
        # Create all tables
        Base.metadata.create_all(bind=db.engine)
        yield app


@pytest.fixture(scope='function')
def client(app: Flask):
    return app.test_client()


@pytest.fixture(scope='function')
def session(app: Flask):
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()

        # Create a new session for testing
        test_session = scoped_session(
            sessionmaker(bind=connection, expire_on_commit=False)
        )

        # Override the default session with our test session
        db.session = test_session

        yield test_session

        # Rollback the transaction and close connections
        transaction.rollback()
        connection.close()
        test_session.remove()
