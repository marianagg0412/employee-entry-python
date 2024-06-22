from db import get_db_connection
from datetime import datetime, timedelta

class GuestService:
    @staticmethod
    def register_guest(guest_name, documento_identidad):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO guest (nombre, documento_identidad) VALUES (%s, %s)",
            (guest_name, documento_identidad)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_guests():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM guests")
        guests = cursor.fetchall()
        cursor.close()
        conn.close()
        return guests
    
    @staticmethod
    def get_employee_entries():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT e.nombre AS guest_name, e.documento_identidad AS guest_id, ee.entry_time, ee.exit_time, e.guest_type as guest_type FROM guest_entries ee JOIN guest e ON ee.guest_id = e.id")
        guests = cursor.fetchall()
        cursor.close()
        conn.close()
        return guests
    
    @staticmethod
    def find_guest_by_documento_identidad(documento_identidad):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM guest WHERE documento_identidad = %s", (documento_identidad,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] if result else None


    @staticmethod
    def record_guest_entry(documento_identidad, entry_time):
        guest_id = GuestService.find_guest_by_documento_identidad(documento_identidad)
        if not guest_id:
            raise ValueError("No guest found with the given documento_identidad")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO guest_entries (guest_id, entry_time) VALUES (%s, %s)",
            (guest_id, entry_time)
        )
        conn.commit()
        cursor.close()
        conn.close()


    @staticmethod
    def record_guest_exit(documento_identidad, exit_time):
        guest_id = GuestService.find_guest_by_documento_identidad(documento_identidad)
        if not guest_id:
            raise ValueError("No guest found with the given documento_identidad")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE guest_entries SET exit_time = %s WHERE guest_id = %s AND exit_time IS NULL",
            (exit_time, guest_id)
        )
        conn.commit()
        cursor.close()
        conn.close()


    @staticmethod
    def get_entries_by_guest(guest_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM guest_entries WHERE guest_id = %s",
            (guest_id,)
        )
        entries = cursor.fetchall()
        cursor.close()
        conn.close()
        return entries
    
    @staticmethod
    def modify_guest(documento_identidad, new_guest_name=None, new_guest_type=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        updates = []
        params = []

        if new_guest_name is not None:
            updates.append("nombre = %s")
            params.append(new_guest_name)
        if new_guest_type is not None:
            updates.append("guest_type = %s")
            params.append(new_guest_type)

        # Only proceed if there are updates to make
        if updates:
            sql_query = "UPDATE guest SET " + ", ".join(updates) + " WHERE documento_identidad = %s"
            params.append(documento_identidad)
            cursor.execute(sql_query, tuple(params))
            conn.commit()

        cursor.close()
        conn.close()




    @staticmethod
    def delete_guest(documento_identidad):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # First, find the guest's ID using documento_identidad
        cursor.execute("SELECT id FROM guest WHERE documento_identidad = %s", (documento_identidad,))
        guest_id = cursor.fetchone()
        if guest_id is None:
            cursor.close()
            conn.close()
            raise ValueError("No guest found with the given documento_identidad")
        
        # Delete entries from guest_entries table
        cursor.execute("DELETE FROM guest_entries WHERE guest_id = %s", (guest_id[0],))
        
        # Now, delete the guest
        cursor.execute("DELETE FROM guest WHERE id = %s", (guest_id[0],))
        
        conn.commit()
        cursor.close()
        conn.close()



