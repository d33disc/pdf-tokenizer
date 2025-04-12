import os
import sys
import argparse
import yaml
from datetime import datetime

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Generate project documentation files.')
    parser.add_argument('-c', '--config', default='docs-config.yml',
                        help='Path to configuration file (default: docs-config.yml)')
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

def load_config(config_path):
    """Load configuration from YAML file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Configuration file not found: {config_path}") from e
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML configuration: {e}") from e

def create_directory_structure(config=None, base_dir='.', verbose=False):
    """Create the necessary directories if they don't exist."""
    # Use directories from config if available, otherwise use default
    if config and 'directories' in config:
        directories = config['directories']
    else:
        directories = ['docs', 'src', 'tests']
        
    for directory in directories:
        full_path = os.path.join(base_dir, directory)
        os.makedirs(full_path, exist_ok=True)
        if verbose:
            print(f"Created directory: {full_path}")

def write_file(filepath, content, force=False, verbose=False):
    """Write content to a file, creating parent directories if needed."""
    # Check if file exists and force flag is not set
    if os.path.exists(filepath) and not force:
        response = input(f"File {filepath} already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
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

def generate_readme_content(config):
    """Generate README content from configuration."""
    if not config or 'project' not in config:
        # Return default README if no config is available
        return DEFAULT_README
    
    project = config['project']
    content = [f"# {project['name']}"]
    
    # Add overview section
    if 'content' in config and 'overview' in config['content']:
        content.append("\n## Overview")
        content.append(config['content']['overview'])
    
    # Add key features section
    if 'content' in config and 'key_features' in config['content']:
        content.append("\n## Key Features")
        for feature in config['content']['key_features']:
            content.append(f"- **{feature['name']}**: {feature['description']}")
    
    # Add quick start section
    if 'content' in config and 'quick_start' in config['content']:
        content.append("\n## Quick Start")
        content.append(config['content']['quick_start'])
    
    # Add performance section
    if 'content' in config and 'performance' in config['content']:
        content.append("\n## Performance")
        for metric in config['content']['performance']:
            content.append(f"- {metric['metric']}: {metric['value']}")
    
    # Add documentation section
    if 'content' in config and 'documentation' in config['content']:
        content.append("\n## Documentation")
        for doc in config['content']['documentation']:
            content.append(f"- [{doc['name']}]({doc['path']})")
    
    # Add license section
    if 'license' in project:
        content.append("\n## License")
        content.append(f"This project is licensed under the {project['license']} License - see the [LICENSE](./LICENSE) file for details.")
    
    return "\n".join(content)

def generate_license_content(config):
    """Generate license content based on configuration."""
    if not config or 'project' not in config:
        return DEFAULT_LICENSE
    
    project = config['project']
    license_type = project.get('license', 'MIT')
    year = project.get('year', datetime.now().year)
    organization = project.get('author', 'Document Processing Project')
    
    if license_type == 'MIT':
        license_text = f"""MIT License

Copyright (c) {year} {organization}

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
SOFTWARE."""
    else:
        # For now, default to MIT if license type is not recognized
        license_text = DEFAULT_LICENSE
        
    return license_text

# Default content for templates
DEFAULT_README = """# High-Performance Document Processing System

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
- [Contributing Guidelines](./docs/CONTRIBUTING.md)

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
"""

DEFAULT_INSTALLATION = """# Installation Guide

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

DEFAULT_USAGE = """# Usage Guide

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

DEFAULT_API = """# API Documentation

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

DEFAULT_CODE_OF_CONDUCT = """# Code of Conduct

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

DEFAULT_CONTRIBUTING = """# Contributing Guidelines

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

DEFAULT_LICENSE = """MIT License

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
        
        # Load configuration if specified
        config = load_config(args.config) if args.config else None
        
        # Create directory structure
        create_directory_structure(config, base_dir=args.output_dir, verbose=args.verbose)

        # Generate content based on configuration or use defaults
        if config:
            readme_content = generate_readme_content(config)
            license_content = generate_license_content(config)
        else:
            readme_content = DEFAULT_README
            license_content = DEFAULT_LICENSE
        
        # Define files and their content
        files = {}
        
        # Skip README if requested
        if not args.skip_readme:
            files['README.md'] = readme_content
        
        # If only README was requested, don't add other files
        if not args.readme_only:
            files.update({
                'docs/INSTALLATION.md': DEFAULT_INSTALLATION,
                'docs/USAGE.md': DEFAULT_USAGE,
                'docs/API.md': DEFAULT_API,
                'CODE_OF_CONDUCT.md': DEFAULT_CODE_OF_CONDUCT,
                'CONTRIBUTING.md': DEFAULT_CONTRIBUTING,
                'LICENSE': license_content
            })

        # Create each file
        generated_files = []
        for filepath, content in files.items():
            if not args.force and os.path.exists(filepath):
                print(f"Conflict detected: {filepath} already exists.")
                try:
                    # Attempt to resolve conflict automatically
                    with open(filepath, 'r', encoding='utf-8') as f:
                        existing_content = f.read()
                    if existing_content == content:
                        print(f"File {filepath} is already up-to-date.")
                        continue
                    else:
                        print(f"File {filepath} has conflicting changes.")
                        response = input(f"Overwrite {filepath}? (y/n): ")
                        if response.lower() != 'y':
                            print(f"Skipping file: {filepath}")
                            continue
                except Exception as e:
                    print(f"Error reading existing file {filepath}: {e}")
                    print("Please resolve the conflict manually.")
                    continue

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
    except Exception as e:
        print(f"Error generating documentation: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

# Usage examples:
# Generate all documentation using configuration file:
#   python generate-docs.py -c docs-config.yml
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
