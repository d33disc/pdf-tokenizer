import os
import sys
import argparse

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Generate project documentation files.')
    parser.add_argument('-o', '--output-dir', default='.', 
                        help='Output directory for generated files (default: current directory)')
    parser.add_argument('-f', '--force', action='store_true',
                        help='Force overwrite of existing files without prompting')
    parser.add_argument('--readme-only', action='store_true',
                        help='Generate only the README.md file')
    parser.add_argument('--skip-readme', action='store_true',
                        help='Skip generating README.md file')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose output')
    
    return parser.parse_args()

def create_directory_structure(base_dir='.', verbose=False):
    """Create the necessary directories if they don't exist."""
    directories = ['docs', 'src', 'tests']
    for directory in directories:
        full_path = os.path.join(base_dir, directory)
        os.makedirs(full_path, exist_ok=True)
        if verbose:
            print(f"Created directory: {full_path}")

def write_file(filepath, content, force=False, verbose=False):
        response = input(f"File {filepath} already exists. Overwrite? (y/n/a/s): ").lower()
        if response == 'y':
            pass  # Proceed with overwrite
        elif response == 'a':
            force = True # Set force to True to overwrite all
        elif response == 's':
            print(f"Skipping file: {filepath}")
            return False
        else:
            print(f"Skipping file: {filepath}")
            return False
    
    dirname = os.path.dirname(filepath)
    if dirname:  # Only try to create directory if there is a directory component
        os.makedirs(dirname, exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    if verbose:
        print(f"Created file: {filepath}")
    return True

# File contents
README_CONTENT = """# High-Performance Document Processing System

## Overview
This project implements a high-performance document processing system with parallel processing capabilities, intelligent caching, and robust error handling. It's designed for processing large volumes of documents efficiently while maintaining reliability and scalability.

## Key Features
- **Parallel Processing**: Efficient multi-core document processing
- **Smart Caching**: Both in-memory and disk-based caching mechanisms
- **Vectorized Operations**: Optimized array operations using NumPy
- **Batch Processing**: Efficient handling of multiple documents
- **Error Recovery**: Comprehensive error handling and logging
- **Performance Monitoring**: Built-in metrics and visualization

## Quick Start
```python
from doc_processor import ParallelDocumentProcessor

# Initialize processor
processor = ParallelDocumentProcessor(max_workers=4)

# Process a document
result = processor.process_document(document_content)
```

## Performance
- Average processing time: 0.075 seconds per document
- Efficient memory usage: < 1MB overhead
- CPU utilization: ~82.5% average

## Documentation
- [Installation Guide](./docs/INSTALLATION.md)
- [Usage Guide](./docs/USAGE.md)
- [API Documentation](./docs/API.md)
- [Contributing Guidelines](./CONTRIBUTING.md)

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
"""

INSTALLATION_CONTENT = """# Installation Guide

## Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

## Step-by-Step Installation

1. **Clone the Repository**
 ```bash
 git clone https://github.com/yourusername/doc-processor.git
 cd doc-processor
 ```

2. **Create and Activate Virtual Environment**
 ```bash
 # On Windows
 python -m venv venv
 .\\venv\\Scripts\\activate

 # On Unix or MacOS
 python3 -m venv venv
 source venv/bin/activate
 ```

3. **Install Dependencies**
 ```bash
 pip install -r requirements.txt
 ```

4. **Verify Installation**
 ```bash
 python -m pytest tests/
 ```

## Dependencies
- numpy>=1.21.0
- pandas>=1.3.0
- psutil>=5.8.0
- matplotlib>=3.4.0
"""

USAGE_CONTENT = """# Usage Guide

## Basic Usage

### Single Document Processing
```python
from doc_processor import ParallelDocumentProcessor

# Initialize processor
processor = ParallelDocumentProcessor(max_workers=4)

# Process a single document
with open('document.txt', 'rb') as f:
  content = f.read()
  result = processor.process_document(content)
```

### Batch Processing
```python
from doc_processor import BatchProcessor

# Initialize batch processor
batch_processor = BatchProcessor(max_batch_size=100)

# Add documents to batch
documents = [doc1, doc2, doc3]
results = batch_processor.process_batch(documents)
```
"""

API_CONTENT = """# API Documentation

## Core Classes

### ParallelDocumentProcessor

```python
class ParallelDocumentProcessor:
  def __init__(self, max_workers: int = None, cache: DocumentCache = None):
      \"\"\"
      Initialize parallel document processor.

      Args:
          max_workers (int, optional): Maximum number of worker processes
          cache (DocumentCache, optional): Custom cache implementation
      \"\"\"

  def process_document(self, content: bytes) -> Dict:
      \"\"\"
      Process a single document in parallel chunks.

      Args:
          content (bytes): Document content to process

      Returns:
          Dict: Processing results
      
      Raises:
          ProcessingError: If processing fails
      \"\"\"
```
"""

CODE_OF_CONDUCT_CONTENT = """# Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members
"""

CONTRIBUTING_CONTENT = """# Contributing Guidelines

## Getting Started

Thank you for considering contributing to our project! This document provides guidelines and instructions for contributing.

### Prerequisites

- Python 3.8 or higher
- Git
- Understanding of parallel processing and document handling

### Setting Up Development Environment

1. Fork the repository
2. Clone your fork:
 ```bash
 git clone https://github.com/your-username/doc-processor.git
 ```
3. Set up development environment:
 ```bash
 cd doc-processor
 python -m venv venv
 source venv/bin/activate  # or `venv\\Scripts\\activate` on Windows
 pip install -r requirements-dev.txt
 ```
"""

LICENSE_CONTENT = """MIT License

Copyright (c) 2025 Document Processing Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

def main():
  """Generate all documentation files."""
  try:
      # Parse command-line arguments
      args = parse_arguments()
      
      # Create directory structure
      create_directory_structure(base_dir=args.output_dir, verbose=args.verbose)

      # Define files and their content
      files = {}
      
      # Skip README if requested
      if not args.skip_readme:
          files['README.md'] = README_CONTENT
      
      # If only README was requested, don't add other files
      if not args.readme_only:
          files.update({
              'docs/INSTALLATION.md': INSTALLATION_CONTENT,
              'docs/USAGE.md': USAGE_CONTENT,
              'docs/API.md': API_CONTENT,
              'CODE_OF_CONDUCT.md': CODE_OF_CONDUCT_CONTENT,
              'CONTRIBUTING.md': CONTRIBUTING_CONTENT,
              'LICENSE': LICENSE_CONTENT
          })

      # Create each file
      generated_files = []
      for filepath, content in files.items():
          full_path = os.path.join(args.output_dir, filepath)
          if write_file(full_path, content, force=args.force, verbose=args.verbose):
              generated_files.append(full_path)

      # Only show summary if not in verbose mode (otherwise it's redundant)
      if not args.verbose:
          print("\nDocumentation files generated successfully!")
      
      if generated_files:
          print("\nGenerated files:")
          for filepath in generated_files:
              print(f"- {filepath}")
      else:
          print("\nNo files were generated.")

  except KeyboardInterrupt:
      print("\nOperation cancelled by user.")
      sys.exit(0)
      import logging
      logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
  except Exception as e:
      logging.error(f"Error generating documentation: {e}", exc_info=True)
      print(f"Error generating documentation: {e}", file=sys.stderr)
      sys.exit(1)

if __name__ == '__main__':
  main()

# Usage examples:
# Generate all documentation to current directory:
#   python generate-docs.py
#
# Generate documentation to a specific directory:
#   python generate-docs.py -o /path/to/project
#
# Generate only README.md:
#   python generate-docs.py --readme-only
#
# Generate all documentation except README.md:
#   python generate-docs.py --skip-readme
#
# Force overwrite of existing files:
#   python generate-docs.py -f
#
# Generate with verbose output:
#   python generate-docs.py -v