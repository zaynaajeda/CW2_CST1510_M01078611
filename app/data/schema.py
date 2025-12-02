def create_users_table(conn):
    """Create users table."""
    #Create cursor
    cursor = conn.cursor()

    #SQL statement to create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    """)

    #Save changes
    conn.commit()
    #Success message
    print("✅ Users table created successfully!")

def create_cyber_incidents_table(conn):
    """Create cyber_incidents table."""
    #Create cursor
    cursor = conn.cursor()

    #SQL statement to create cyber_incidents table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cyber_incidents(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            incident_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            incident_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT NOT NULL,
            description TEXT,
            reported_by TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    #Save changes 
    conn.commit()
    #Success message
    print("✅ cyber_incidents table created successfully!")

def create_datasets_metadata_table(conn):
    """Create datasets_metadata table."""
    #Create cursor
    cursor = conn.cursor()

    #SQL statement to create datasets_metadata table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datasets_metadata(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dataset_name TEXT NOT NULL,
            category TEXT NOT NULL,
            source TEXT,
            last_updated TEXT,
            record_count INTEGER,
            file_size_mb REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    #Save changes 
    conn.commit()
    #Success message
    print("✅ datasets_metadata table created successfully!")

def create_it_tickets_table(conn):
    """Create it_tickets table."""
    #Create cursor
    cursor = conn.cursor()

    #SQL statement to create it_tickets table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS it_tickets(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id TEXT UNIQUE NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL,
            category TEXT NOT NULL,
            subject TEXT NOT NULL,
            description TEXT,
            created_date TEXT NOT NULL,
            resolved_date TEXT,
            assigned_to TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    #Save changes 
    conn.commit()
    #Success message
    print("✅ it_tickets table created successfully!")

def create_all_tables(conn):
    """Create all tables."""
    create_users_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)