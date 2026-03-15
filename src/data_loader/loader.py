# src/data_loader/loader.py
# This file is part of the 2FAS iOS app
# This module defines functions for loading data from CSV files into a SQLite database,
# as well as providing a utility function to get a
# database connection for querying analytics data.

import sqlite3
import pandas as pd
from src.utils.config import DB_PATH, USERS_CSV, USAGE_CSV, SYSTEM_CSV, TICKETS_CSV

def load_csvs():
    users = pd.read_csv(USERS_CSV, parse_dates=["signup_date"])
    usage = pd.read_csv(USAGE_CSV, parse_dates=["timestamp"])
    system = pd.read_csv(SYSTEM_CSV, parse_dates=["timestamp"])
    tickets = pd.read_csv(TICKETS_CSV, parse_dates=["created_at", "resolved_at"])
    return users, usage, system, tickets

def init_sqlite():
    users, usage, system, tickets = load_csvs()
    conn = sqlite3.connect(DB_PATH)
    users.to_sql("users", conn, if_exists="replace", index=False)
    usage.to_sql("usage_events", conn, if_exists="replace", index=False)
    system.to_sql("system_events", conn, if_exists="replace", index=False)
    tickets.to_sql("tickets", conn, if_exists="replace", index=False)
    conn.close()

def get_connection():
    return sqlite3.connect(DB_PATH)
