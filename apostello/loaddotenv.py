#!/usr/bin/env python
import os

from dotenv import load_dotenv


def loaddotenv():
    fname = '.env'
    dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', fname))
    load_dotenv(dotenv_path)
