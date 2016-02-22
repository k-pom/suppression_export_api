#!/usr/bin/env python
"""
    This file is what runs every 5 minutes on the heroku scheduler

    TODO: Move this into a fabric/paver command
"""
from exporter.logic import exports

exports.process_pending()
