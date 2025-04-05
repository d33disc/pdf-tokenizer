# Installation Guide

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
 .\venv\Scripts\activate

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
