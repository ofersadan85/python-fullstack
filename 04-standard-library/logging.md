# Python `logging` module - basic examples

The `logging` module helps you print structured runtime messages (debug, info, warnings, and errors).

## 1. Basic logging setup

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("App started")
logging.warning("Low disk space")
```

## 2. Logging levels

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug details")
logging.info("General information")
logging.warning("Something unexpected happened")
logging.error("An error occurred")
logging.critical("Serious failure")
```

## 3. Add timestamps and level names

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logging.info("User logged in")
```

## 4. Log to a file

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logging.info("Saved order #123")
```

## 5. Use a named logger

```python
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
logger.info("Running module code")
```

## 6. Log exceptions with traceback

```python
import logging

logging.basicConfig(level=logging.INFO)

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("Calculation failed")
```

## 7. Named logger with different outputs (stdout + file)

```python
import logging
import sys

logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)  # Collect all levels; handlers decide what to output
logger.propagate = False

formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

# Handler 1: stdout (INFO and above)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(formatter)

# Handler 2: file (DEBUG and above)
file_handler = logging.FileHandler("my_app.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(stdout_handler)
logger.addHandler(file_handler)

logger.debug("Loaded configuration file")   # File only
logger.info("Service started successfully") # Stdout + file
logger.warning("Cache miss ratio is high")  # Stdout + file
```

> [!NOTE]
> Prefer `logging` over `print()` for real applications: it supports levels, formatting, and writing logs to files or external systems.
