#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue 21 Jun 2022 09:53:20 AM CEST

@author hielke
"""

from fastapi.testclient import TestClient

from src.serve_model import app

client = TestClient(app)


def test_read_main():
    response = client.get("/metrics/")
    assert response.status_code == 200
