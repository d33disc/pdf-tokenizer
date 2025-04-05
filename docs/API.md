# API Documentation

## Core Classes

### ParallelDocumentProcessor

```python
class ParallelDocumentProcessor:
  def __init__(self, max_workers: int = None, cache: DocumentCache = None):
      """
      Initialize parallel document processor.

      Args:
          max_workers (int, optional): Maximum number of worker processes
          cache (DocumentCache, optional): Custom cache implementation
      """

  def process_document(self, content: bytes) -> Dict:
      """
      Process a single document in parallel chunks.

      Args:
          content (bytes): Document content to process

      Returns:
          Dict: Processing results
      
      Raises:
          ProcessingError: If processing fails
      """
```
