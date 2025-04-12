# PDF Tokenization Benchmarks

## Overview

This document provides performance benchmarks for the PDF Tokenizer library across various document types and processing scenarios. These benchmarks were measured on a standard system with the following specifications:

- CPU: Intel Core i7-9750H (6 cores, 12 threads)
- RAM: 16GB DDR4
- Storage: NVMe SSD
- OS: Ubuntu 20.04 LTS

## Processing Speed

| Document Type | Size (Pages) | Size (MB) | Processing Time (s) | Throughput (pages/s) |
|---------------|--------------|-----------|---------------------|----------------------|
| Text-only     | 10           | 0.5       | 0.75                | 13.33                |
| Text-only     | 100          | 4.2       | 6.82                | 14.66                |
| Text + Images | 10           | 2.3       | 1.21                | 8.26                 |
| Text + Images | 100          | 22.5      | 11.45               | 8.73                 |
| Forms         | 10           | 1.8       | 1.93                | 5.18                 |
| Scanned (OCR) | 10           | 15.6      | 32.45               | 0.31                 |

## Memory Usage

| Document Type | Size (Pages) | Peak Memory (MB) | Avg Memory (MB) |
|---------------|--------------|------------------|-----------------|
| Text-only     | 10           | 78               | 52              |
| Text-only     | 100          | 205              | 145             |
| Text + Images | 10           | 112              | 85              |
| Text + Images | 100          | 382              | 264             |
| Forms         | 10           | 95               | 63              |
| Scanned (OCR) | 10           | 725              | 510             |

## Tokenization Strategy Comparison

| Strategy      | Document Size | Processing Time (s) | Memory Usage (MB) | Token Count |
|---------------|---------------|---------------------|-------------------|-------------|
| Basic         | 50 pages      | 3.42                | 112               | 24,532      |
| Semantic      | 50 pages      | 4.21                | 145               | 8,762       |
| ML-Ready      | 50 pages      | 5.67                | 215               | 12,341      |

## Parallel Processing Performance

| CPU Cores | Documents | Total Pages | Processing Time (s) | Speedup |
|-----------|-----------|-------------|---------------------|---------|
| 1         | 10        | 500         | 42.35               | 1.00×   |
| 2         | 10        | 500         | 23.61               | 1.79×   |
| 4         | 10        | 500         | 12.42               | 3.41×   |
| 8         | 10        | 500         | 7.21                | 5.87×   |
| 12        | 10        | 500         | 5.63                | 7.52×   |

## Format Compatibility

| PDF Version | Format Features                    | Compatibility | Notes                                |
|-------------|-----------------------------------|---------------|--------------------------------------|
| PDF 1.0-1.4 | Basic text, images                | 100%          | Full support                         |
| PDF 1.5     | Object streams, XRef streams      | 100%          | Full support                         |
| PDF 1.6     | AES encryption, NChannel          | 95%           | Some advanced graphics limitations   |
| PDF 1.7     | 3D content, rich media            | 90%           | Limited 3D content support           |
| PDF 2.0     | Geospatial features               | 85%           | Some newer features not fully supported |

## Accuracy Metrics

| Document Type    | Extraction Accuracy | Structure Preservation | Table Recognition |
|------------------|---------------------|------------------------|-------------------|
| Academic papers  | 98.7%               | 95.2%                  | 92.1%             |
| Legal documents  | 99.2%               | 97.5%                  | 96.3%             |
| Financial reports| 98.5%               | 94.8%                  | 98.2%             |
| Technical manuals| 97.9%               | 93.5%                  | 90.7%             |
| Scanned (OCR)    | 92.3%               | 85.1%                  | 78.4%             |

## Comparison with Other Libraries

| Library       | Speed (relative) | Memory Usage | Feature Support | Accuracy |
|---------------|------------------|--------------|-----------------|----------|
| PDF Tokenizer | 1.00×            | 1.00×        | ★★★★★            | 97.5%    |
| PyPDF2        | 1.35×            | 0.72×        | ★★★☆☆            | 92.1%    |
| PDFMiner      | 0.65×            | 1.25×        | ★★★★☆            | 96.8%    |
| Tika          | 0.58×            | 1.85×        | ★★★★☆            | 95.4%    |
| pdftotext     | 1.68×            | 0.45×        | ★★☆☆☆            | 91.2%    |

## Resource Optimization

| Optimization Technique | Speed Improvement | Memory Reduction | When to Use                       |
|------------------------|-------------------|------------------|-----------------------------------|
| Batch processing       | Up to 40%         | 15-25%           | Processing multiple documents     |
| Page filtering         | Up to 90%         | 50-80%           | When only specific pages needed   |
| Content filtering      | Up to 75%         | 30-60%           | When only specific content needed |
| Memory mapping         | 5-10%             | 60-70%           | For very large documents          |
| Caching                | Up to 95%         | None             | For repeated access               |

## Conclusions

- PDF Tokenizer offers excellent performance for most common PDF processing tasks
- Parallel processing provides near-linear speedup up to 4 cores
- Memory usage scales approximately linearly with document size
- Performance and memory usage vary significantly based on document content type
- OCR processing for scanned documents is significantly more resource-intensive
- Specialized tokenization strategies trade performance for different features
