#!/usr/bin/env python3
"""
Progress bar utilities for CLI tools
"""

import sys
import time


def progress_bar(current, total, prefix='Progress:', suffix='Complete', bar_length=50):
    """
    Display a progress bar in the console.
    
    Args:
        current: Current progress (0 to total)
        total: Total items to process
        prefix: Text before the bar
        suffix: Text after the percentage
        bar_length: Length of the progress bar
    """
    if total == 0:
        return
        
    fraction = min(current / total, 1.0)
    filled = int(fraction * bar_length)
    bar = '█' * filled + '░' * (bar_length - filled)
    percent = int(fraction * 100)
    
    ending = '\n' if current >= total else '\r'
    print(f'{prefix} [{bar}] {percent}% {suffix}', end=ending)
    sys.stdout.flush()


class ProgressTracker:
    """Track progress through multiple steps"""
    
    def __init__(self, total_steps, quiet=False):
        self.total = total_steps
        self.current = 0
        self.quiet = quiet
        
    def step(self, message=''):
        """Advance to next step"""
        self.current += 1
        if not self.quiet:
            progress_bar(self.current, self.total, prefix='Steps:', suffix=message)
            
    def finish(self):
        """Mark as complete"""
        if not self.quiet:
            progress_bar(self.total, self.total, prefix='Complete:')


# Demo
if __name__ == '__main__':
    print("Demo: Progress bar")
    for i in range(101):
        progress_bar(i, 100, prefix='Processing:', suffix='Files')
        time.sleep(0.01)
    
    print("\nDemo: Step tracker")
    tracker = ProgressTracker(5)
    for step in ['Init', 'Load', 'Process', 'Save', 'Cleanup']:
        time.sleep(0.2)
        tracker.step(step)
