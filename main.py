from app.data.db import connect_database, load_csv_to_table
from app.data.schema import create_all_tables
from pathlib import Path

def main():
    print("=" * 60)
    print("Week 8: Database Demo")
    print("=" * 60)
    
    DB_DIR = Path("DATA")

    # 1. Setup database
    conn = connect_database()
    create_all_tables(conn)
    #conn.close()
    
    load_csv_to_table(conn, DB_DIR / "cyber_incidents.csv", "cyber_incidents")
    load_csv_to_table(conn, DB_DIR / "datasets_metadata.csv", "datasets_metadata")
    load_csv_to_table(conn, DB_DIR / "it_tickets.csv", "it_tickets")

    from app.services.user_service import register_user, login_user, migrate_users_from_file
    from app.data.incidents import insert_incident, get_all_incidents
    from app.data.datasets import get_all_datasets, insert_dataset
    
    # 2. Migrate users
    migrate_users_from_file(conn, DB_DIR / "users.txt")
    
    # 3. Test authentication
    success, msg = register_user("anna", "SecurePass123!", "analyst")
    print(msg)
    
    success, msg = login_user("anna", "SecurePass123!")
    print(msg)
    
    # 4. Test CRUD
    incident_id = insert_incident(
        "2024-11-05",
        "Phishing",
        "High",
        "Open",
        "Suspicious email detected",
        "alice"
    )
    print(f"Created incident #{incident_id}")
    
    # 5. Query data
    df = get_all_incidents()
    print(f"Total incidents: {len(df)}")

    #Test CRUD for datasets
    dataset_id = insert_dataset(
        "Employee Records",
        5000,
        "HR Department",
        "2024-10-20",
        10,
        2.5,
        "Personnel"
    )
    print(f"Created dataset #{dataset_id}")

    #Query datasets
    df_datasets = get_all_datasets()
    print(f"Total datasets: {len(df_datasets)}")

    conn.close()
if __name__ == "__main__":
    main()