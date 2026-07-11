#!/usr/bin/env python
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
