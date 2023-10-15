from datetime import datetime, timedelta
from app.services.token_manager import generate_delete_token, validate_delete_token

def test_delete_token():
    # Step 1: Generate a delete token.
    token = generate_delete_token()

    # Step 2: Validate it. The token should be valid.
    assert validate_delete_token(token) == True

    # Step 3: Generate an invalid token using a random value.
    invalid_token = "random_invalid_value"

    # Step 4: Validate the invalid token. The validation should fail.
    assert validate_delete_token(invalid_token) == False

    # Step 5: Generate a token with a datetime from the past.
    past_time = datetime.utcnow() - timedelta(minutes=10)  # 10 minutes in the past
    past_token = generate_delete_token(past_time)

    # Step 6: Validate this past token. The validation should fail.
    assert validate_delete_token(past_token) == False
