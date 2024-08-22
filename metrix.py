from datetime import datetime
from openpaygo import MetricsRequestHandler, AuthMethod



metrics_request = MetricsRequestHandler(
    serial_number='296825781',
    secret_key='65715222cf186ee48ba8655e99c5b91c',
    auth_method=AuthMethod.SIMPLE_AUTH
)

metrics_request.set_timestamp(datetime.now().timestamp())
metrics_request.set_data({
    "token_count": 1,
    "tampered": False,
    "firmware_version": '1.0.0',
})

paygo_metrics_payload = metrics_request.get_simple_request_payload()

print(paygo_metrics_payload)
