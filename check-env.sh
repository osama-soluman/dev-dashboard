#!/bin/bash
echo "=== AI Engineering Environment Check ==="
echo "python version: $(python3 --version)"
echo "git branch: $(git branch --show-current 2>/dev/null || echo 'no git repo')"
echo "virtual env active: ${VIRTUAL_ENV:-not active}"
echo "========================================"
