```python
import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise EnvironmentError(f"Variable '{key}' non trouvée dans.env")
    return value
```
