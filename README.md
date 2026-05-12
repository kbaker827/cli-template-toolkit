# cli-template-toolkit

OpenClaw skill toolkit with reusable Python CLI templates and patterns extracted from 12+ tools via Ralph Loop.

## Contents

- `scripts/argparse_boilerplate.py` - Standard argparse setup with subcommands, help formatting, and config file support
- `scripts/colored_logger.py` - Colored console logging with log level filtering
- `scripts/progress_utils.py` - CLI progress bars and spinner utilities

## Usage

```python
from scripts.argparse_boilerplate import build_parser
from scripts.colored_logger import get_logger
from scripts.progress_utils import ProgressBar
```

## Related

- [api-client-toolkit](https://github.com/kbaker827/api-client-toolkit)
- [gui-template-toolkit](https://github.com/kbaker827/gui-template-toolkit)
- [ralph-loop](https://github.com/kbaker827/ralph-loop)
