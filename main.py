#!/usr/bin/env python3

from scripts import logCleaner

raw_logs = logCleaner.Load_data()
logCleaner.See_data(raw_logs)
