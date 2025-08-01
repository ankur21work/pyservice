import pytest
import allure

@allure.suite("[Automated] Login Module")
@allure.step("Perform login with username: {username} and password: {password}")
def login(username, password):
    """Simulates a user login."""
    print(f"Logging in user: {username}")
    if username == "user" and password == "pass":
        allure.attach("Login successful screenshot", name="login_success", attachment_type=allure.attachment_type.PNG)
        return True
    else:
        allure.attach("Login failed screenshot", name="login_failure", attachment_type=allure.attachment_type.PNG)
        pytest.fail("Login failed")

@allure.step("Navigate to dashboard")
def navigate_to_dashboard():
    """Simulates navigating to the dashboard."""
    print("Navigating to dashboard...")
    assert True

@allure.step("Verify user is logged in")
def verify_login_status():
    """Checks if the user is logged in."""
    print("Verifying login status...")
    assert True

@allure.step("Attempting invalid login")
def attempt_invalid_login(username, password):
    print(f"Attempting invalid login for user: {username}")
    assert username != "user" or password != "pass", "Expected invalid credentials"

@pytest.mark.smoke
@allure.title("Test for successful login")
def test_successful_login_flow():
    """A test case demonstrating a successful login flow with steps."""
    login("user", "pass")
    navigate_to_dashboard()
    verify_login_status()
@allure.title("Test for invalid login")
def test_invalid_login_flow():
    """A test case demonstrating an invalid login flow with steps."""
    with pytest.raises(Exception): # Expecting an exception due to failed login
        login("wrong_user", "wrong_pass")
    attempt_invalid_login("wrong_user", "wrong_pass")
