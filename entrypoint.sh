#!/bin/bash

xvfb-run poetry run uvicorn --host 0.0.0.0 app.main:app