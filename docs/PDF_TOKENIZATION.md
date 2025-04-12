# PDF Tokenization Guide

## Overview

PDF Tokenizer is designed to efficiently extract and process text content from PDF documents. It handles various PDF complexities including different encodings, embedded images, complex layouts, and security features.

## Supported PDF Features

- **Text Extraction**: Extract plain text from PDF documents
- **Structure Preservation**: Maintain paragraph and section structure
- **Table Recognition**: Identify and extract tabular data
- **Multi-column Support**: Handle complex page layouts
- **Font Information**: Preserve font styles and sizes when needed
- **Embedded Images**: Extract and reference image content
- **Form Fields**: Extract data from PDF forms
- **OCR Integration**: Process scanned documents via OCR

## Tokenization Strategies

### Basic Tokenization

The most straightforward approach, splitting text into words:

```python
from pdf_tokenizer import PDFTokenizer

tokenizer = PDFTokenizer(strategy='basic')
tokens = tokenizer.tokenize('document.pdf')

# Result example: ['This', 'is', 'a', 'sample', 'PDF', 'document']
```

### Semantic Tokenization

More advanced tokenization that preserves semantic units:

```python
tokenizer = PDFTokenizer(strategy='semantic')
tokens = tokenizer.tokenize('document.pdf')

# Result example: ['This is', 'a sample', 'PDF document']
```

### ML-Ready Tokenization

Specialized tokenization for machine learning applications:

```python
tokenizer = PDFTokenizer(strategy='ml', 
                        max_length=512, 
                        stride=128)
tokens = tokenizer.tokenize('document.pdf')

# Result includes tokens with position information and other metadata
```

## Handling PDF Challenges

### Large Documents

For PDFs with many pages:

```python
tokenizer = PDFTokenizer(batch_size=10)  # Process 10 pages at a time
tokens = tokenizer.tokenize('large_document.pdf')
```

### Password-Protected PDFs

For secured documents:

```python
tokenizer = PDFTokenizer()
tokens = tokenizer.tokenize('secured_document.pdf', password='document_password')
```

### Scanned Documents

For PDFs that are essentially images:

```python
tokenizer = PDFTokenizer(use_ocr=True, ocr_language='eng')
tokens = tokenizer.tokenize('scanned_document.pdf')
```

## Performance Considerations

- **Memory Usage**: Typically 50-100MB per document, depending on size and complexity
- **Processing Speed**: ~0.2 seconds per page on modern hardware
- **Scaling**: Use parallel processing for batch operations (built-in)
- **Caching**: Enable result caching to improve performance for repeated operations

## Integration with Machine Learning

### Text Classification

```python
from pdf_tokenizer import PDFTokenizer
from pdf_tokenizer.ml import TextClassifier

tokenizer = PDFTokenizer(strategy='ml')
classifier = TextClassifier(model='bert-base-uncased')

tokens = tokenizer.tokenize('document.pdf')
category = classifier.classify(tokens)
```

### Named Entity Recognition

```python
from pdf_tokenizer.ml import EntityRecognizer

recognizer = EntityRecognizer()
entities = recognizer.extract_entities(tokens)

# Result example: {'persons': ['John Smith'], 'organizations': ['Acme Corp']}
```

## Best Practices

1. **Pre-processing**: Clean and normalize PDFs before tokenization when possible
2. **Batching**: Process documents in batches for optimal performance
3. **Selective Extraction**: Only extract the sections or pages you need
4. **Caching**: Cache results for frequently accessed documents
5. **Error Handling**: Implement robust error handling for problematic documents

## Limitations

- Complex mathematical formulas may not tokenize correctly
- Some highly specialized PDF features might not be supported
- Documents with custom encoding might require special handling
- Extremely large documents may require streaming processing
