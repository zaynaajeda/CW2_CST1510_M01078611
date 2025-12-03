import sqlite3
from pathlib import Path
import os
import pandas as pd

DB_PATH = Path("DATA") / "intelligence_platform.db"

def connect_database(db_path=DB_PATH):
    """
    Connect to the SQLite database.
    Creates the database file if it doesn't exist.

    Args:
        db_path: Path to the database file

    Returns:
        sqlite3.Connection: Database connection object
    """
    return sqlite3.connect(str(db_path))

#CSV loading function
def load_csv_to_table(conn, csv_path, table_name):
  #Checks if CSV file exists
  if os.path.exists(csv_path):
    #Print success message
    print(f"Success: CSV file was found at {csv_path}")
  else:
    #Print error message
    print(f"Error: No CSV file was found at {csv_path}")
    #No rows were loaded into SQL table
    return 0

  #Read CSV file using pandas
  df = pd.read_csv(csv_path)

  #Rename columns for cyber_incidents table
  if table_name == "cyber_incidents":
    df = df.rename(columns = {
        "timestamp": "date",
        "category": "incident_type",
        "incident_id": "id"
    })

    if "reported_by" not in df.columns:
      #Insert reported_by column with default data
      df["reported_by"] = "Unknown"

  #Rename columns for datasets_metadata table
  if table_name == "datasets_metadata":
    df = df.rename(columns={
      "dataset_id" : "id",
      "name" : "dataset_name",
      "rows" : "record_count",
      "uploaded_by" : "source",
      "upload_date" : "last_updated",
      "columns" : "column_count",
    })

    #Function to assign category based on dataset name
    def assign_category(name):
      #Make name lowercase to prevent case sensitivity errors
      name = name.lower()
      #Verify if fraud is in name
      if "fraud" in name:
        #Assign category
        return "Threat Intelligence"
      
      #Verify if server or logs is in name
      if "server" in name or "logs" in name:
        #Assign category
        return "Network Logs"
      
      #Verify if churn or customer is in name
      if "churn" in name or "customer" in name:
        #Assign category
        return "Customer Analytics"
      
      #Verify if name or classification is in name
      if "name" in name or "classification" in name:
        #Assign category
        return "Image Data"
      
      #Verify if salary or hr is in name
      if "salary" in name or "hr" in name:
        #Assign category
        return "HR Data"
      
      #Assign category as General if no keywords found
      return "General"
    
    #Apply function to dataset_name column to create category column
    df["category"] = df["dataset_name"].apply(assign_category)

    #Missing columns handling
    if "file_size_mb" not in df.columns:
      #Insert file_size_mb column with default data
      df["file_size_mb"] = "Unknown"

  #Rename columns for it_tickets table
  if table_name == "it_tickets":
    df = df.rename(columns={
      "ticket_id" : "id",
      "resolution_time_hours" : "resolved_date",
      "created_at" : "created_date",
    })

    #Missing columns handling
    if "category" not in df.columns:
      #Insert category column with default data
      df["category"] = "General"

    if "subject" not in df.columns:
      #Insert subject column with default data
      df["subject"] = "No Subject"

  #Error handling
  try:
    #Insert data into sql table
    rows_count = df.to_sql(name = table_name, con = conn, if_exists = 'append', index = False)
    #Print success message
    print(f"{rows_count} added from {csv_path} to {table_name}")
  except Exception as e:
    #Print error message
    print(e)
    #No rows added since Exception is raised
    return 0

  #Number of rows loaded into sql table is returned
  return rows_count