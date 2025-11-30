#!/usr/bin/env python3
import streamlit as st
import os
import sys
import json
import requests
from datetime import datetime
from typing import Dict, Any, Optional

# Add agents to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import all agents
from agents.ghc_dt import run_ghc_dt
...
if __name__ == "__main__":
    main()
