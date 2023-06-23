import uuid
import clipboard as cp

uuid_str = str(uuid.uuid4())

name = 'name="omron_virual"'
driver = 'driver="omron"'
validator_uuid = f'validator_uuid="{uuid_str}"'
address = 'address="127.0.0.1:9999"'

tar_str = f'validator_m.create({{{name}, {driver}, {validator_uuid}, {address}}})'

cp.copy(str(tar_str.replace("'", "")))

