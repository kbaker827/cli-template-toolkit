#!/usr/bin/env python3
"""
Full-featured argparse CLI template
"""

import argparse
import sys
from pathlib import Path


def create_parser():
    """Create and configure argument parser"""
    parser = argparse.ArgumentParser(
        description='CLI Tool Description',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s input.txt
  %(prog)s input.txt -o output.txt -v
  %(prog)s --version
        '''
    )
    
    # Positional arguments
    parser.add_argument('input', 
                       help='Input file or directory')
    
    # Optional arguments
    parser.add_argument('-o', '--output',
                       help='Output file (default: auto-generated)')
    
    parser.add_argument('-v', '--verbose',
                       action='store_true',
                       help='Enable verbose output')
    
    parser.add_argument('-q', '--quiet',
                       action='store_true',
                       help='Suppress non-error output')
    
    parser.add_argument('--dry-run',
                       action='store_true',
                       help='Show what would be done without making changes')
    
    parser.add_argument('--version',
                       action='version',
                       version='%(prog)s 1.0.0')
    
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    
    # Validate input
    if not Path(args.input).exists():
        print(f"Error: Input not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    
    # Main logic here
    if not args.quiet:
        print(f"Processing: {args.input}")
    
    # Success
    return 0


if __name__ == '__main__':
    sys.exit(main())
