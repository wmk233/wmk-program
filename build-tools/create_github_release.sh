#!/bin/bash
# GitHub Release Script for Watermark Tool

# 创建GitHub Release并上传可执行文件
gh release create v1.0.0 \
  --title "Watermark Tool v1.0.0" \
  --notes "Initial release of Watermark Tool with full Chinese watermark support.

Features:
- Text watermark with Chinese character support (fixed encoding issues)
- Image watermark
- Position control (9 preset positions + custom drag)
- Opacity and size adjustment
- Batch processing
- Template saving/loading
- Cross-platform support (Windows/macOS)

Windows executable included in this release." \
  "release/watermark-tool-windows-v1.0.0-chinese-fix.zip"