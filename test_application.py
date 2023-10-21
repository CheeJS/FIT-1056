import pytest
from application_layer import Application


# Create a fixture for your Application class to use in test cases
@pytest.fixture
def app():
    return Application(master=None, width=960, height=540)

def test_load_users_success(app):
    # Test the load_users method
    app.load_users()
    # Assert that users are loaded correctly
    assert len(app.all_users) > 0


def test_load_users_fail(app):
    # Set an invalid file path
    app.file_path = "./data/fakefile.txt"
    with pytest.raises(FileNotFoundError):
        # Try to load users from the invalid file
        app.load_users()


if __name__ == "__main__":
    pytest.main()
