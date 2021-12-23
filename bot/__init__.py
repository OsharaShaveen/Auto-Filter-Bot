#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @WhiteDevilOp999

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("5866033"))

API_HASH = os.environ.get("42d7a2ab1846d9f5a0e4964f99f597f7")

BOT_TOKEN = os.environ.get("5078880453:AAHv3yGXmkp1Mp5aTM4ABWkdfTuGUbvuHFc")

DB_URI = os.environ.get("mongodb+srv://osmedia:osmedia@cluster0.eyxeo.mongodb.net/osmedia?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("BQBDRO8evPEoMlXoUnQ7LLO_cT-OtM9zZDQCuAinBmbzJPaQsmGviVghkavL0XHW6mCewGPeKnBhrY4BWh5I594xuDmq6Iuufx8cxvgtyEJFBu3eVAS3jFLMF0d7oPO0Dk8NnOgFDoybXyM2MMJB2z3_xzFhEKw1ixFUmYZcSB0ox8QdWG1UBv-ZVJfookOursVLWdLoE-BJixKufq-9nbqFU2YfI_rH-ez-nQ0JLRi_s_k97kS9pbJuYMyPJEkJFGa9c6YH8hIyD1yR6BplIrUFXOqJxs2xxEcAnmJNDboyePS0u-5yvv-clA02zUkeIaznzf1XRwL4bqebDei-PuuEdVr6eQA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
