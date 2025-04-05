# Usage Guide

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
