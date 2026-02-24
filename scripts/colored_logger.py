#!/usr/bin/env python3
"""
Color-coded logging for CLI tools
"""

import sys
from datetime import datetime


class Colors:
    """ANSI color codes"""
    OK = '\033[92m'      # Green
    WARN = '\033[93m'    # Yellow  
    ERROR = '\033[91m'   # Red
    INFO = '\033[94m'    # Blue
    DEBUG = '\033[90m'   # Gray
    END = '\033[0m'      # Reset


class Logger:
    """Simple colored logger"""
    
    def __init__(self, quiet=False, verbose=False):
        self.quiet = quiet
        self.verbose = verbose
        
    def _timestamp(self):
        return datetime.now().strftime("%H:%M:%S")
        
    def debug(self, msg):
        if self.verbose and not self.quiet:
            print(f"[{self._timestamp()}] {Colors.DEBUG}[DBG]{Colors.END} {msg}")
            
    def info(self, msg):
        if not self.quiet:
            print(f"[{self._timestamp()}] {Colors.INFO}[INF]{Colors.END} {msg}")
            
    def ok(self, msg):
        if not self.quiet:
            print(f"[{self._timestamp()}] {Colors.OK}[OK]{Colors.END} {msg}")
            
    def warn(self, msg):
        if not self.quiet:
            print(f"[{self._timestamp()}] {Colors.WARN}[WRN]{Colors.END} {msg}")
            
    def error(self, msg):
        print(f"[{self._timestamp()}] {Colors.ERROR}[ERR]{Colors.END} {msg}", file=sys.stderr)


# Convenience functions for simple usage
def log_ok(msg): Logger().ok(msg)
def log_warn(msg): Logger().warn(msg)
def log_error(msg): Logger().error(msg)
def log_info(msg): Logger().info(msg)
def log_debug(msg): Logger(verbose=True).debug(msg)


if __name__ == '__main__':
    # Demo
    log = Logger()
    log.info("Starting process...")
    log.ok("Step 1 complete")
    log.warn("This might be slow")
    log.error("Something went wrong")
