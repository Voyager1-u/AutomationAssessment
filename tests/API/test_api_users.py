import sys
import os
import requests

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../")
    )
)




from utils.logger import get_logger
logger = get_logger("api_logs")

BASE_URL = "https://reqres.in/api"

HEADERS = {
    "x-api-key": "free_user_3EMX1W2IKxeqHr1n0m6VVTZliCj"
}


# -------------------------
# CREATE USER
# -------------------------
def test_create_user():

    logger.info("START: Create User Test")

    payload = {
        "name": "Uday",
        "job": "QA Engineer"
    }

    logger.info(f"Request Payload: {payload}")

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload,
        headers=HEADERS
    )

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.text}")

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["name"] == "Uday"
    assert response_data["job"] == "QA Engineer"

    logger.info("END: Create User Test PASSED")


# -------------------------
# GET USER
# -------------------------
def test_get_user():

    logger.info("START: Get User Test")

    response = requests.get(
        f"{BASE_URL}/users/2",
        headers=HEADERS
    )

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.text}")

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["data"]["id"] == 2

    logger.info("END: Get User Test PASSED")


# -------------------------
# UPDATE USER
# -------------------------
def test_update_user():

    logger.info("START: Update User Test")

    payload = {
        "name": "Uday Updated",
        "job": "Senior QA"
    }

    logger.info(f"Request Payload: {payload}")

    response = requests.put(
        f"{BASE_URL}/users/2",
        json=payload,
        headers=HEADERS
    )

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.text}")

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["name"] == "Uday Updated"
    assert response_data["job"] == "Senior QA"

    logger.info("END: Update User Test PASSED")


# -------------------------
# DELETE USER
# -------------------------
def test_delete_user():

    logger.info("START: Delete User Test")

    response = requests.delete(
        f"{BASE_URL}/users/2",
        headers=HEADERS
    )

    logger.info(f"Response Status Code: {response.status_code}")

    assert response.status_code == 204

    logger.info("END: Delete User Test PASSED")


# ==================================================
# NEGATIVE TEST CASES
# ==================================================

def test_invalid_endpoint():

    logger.info("START: Invalid Endpoint Test")

    response = requests.get(
        f"{BASE_URL}/invalidendpoint",
        headers=HEADERS
    )

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.text}")

    assert response.status_code in [200, 404]

    logger.info("END: Invalid Endpoint Test PASSED")


def test_invalid_payload():

    logger.info("START: Invalid Payload Test")

    payload = "invalid_data"

    response = requests.post(
        f"{BASE_URL}/users",
        data=payload,
        headers=HEADERS
    )

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.text}")

    assert response.status_code in [201, 400]

    logger.info("END: Invalid Payload Test PASSED")


def test_non_existing_user():

    logger.info("START: Non Existing User Test")

    response = requests.get(
        f"{BASE_URL}/users/999",
        headers=HEADERS
    )

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.text}")

    assert response.status_code == 404

    logger.info("END: Non Existing User Test PASSED")