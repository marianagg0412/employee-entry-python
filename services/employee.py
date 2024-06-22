# services/employee.py
from db import get_db_connection
from datetime import datetime, timedelta

class EmployeeService:
    @staticmethod
    def register_employee(nombre, documento_identidad, area):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employee (nombre, documento_identidad, area) VALUES (%s, %s, %s)",
            (nombre, documento_identidad, area)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_employees():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employee")
        employees = cursor.fetchall()
        cursor.close()
        conn.close()
        return employees
    
    @staticmethod
    def get_employee_entries():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT e.nombre AS employee_name, e.documento_identidad AS employee_id, ee.entry_time, ee.exit_time, ee.motivo_retiro, e.area AS employee_area FROM employee_entries ee JOIN employee e ON ee.employee_id = e.id")
        employees = cursor.fetchall()
        cursor.close()
        conn.close()
        return employees
    
    @staticmethod
    def find_employee_by_documento_identidad(documento_identidad):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM employee WHERE documento_identidad = %s", (documento_identidad,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return result[0]  # Return the employee ID
        else:
            return None  # Return None if no employee found

    @staticmethod
    def record_employee_entry(documento_identidad, entry_time):
        employee_id = EmployeeService.find_employee_by_documento_identidad(documento_identidad)
        if employee_id is None:
            raise ValueError("Employee not found with the given documento_identidad.")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employee_entries (employee_id, entry_time) VALUES (%s, %s)",
            (employee_id, entry_time)
        )
        conn.commit()
        cursor.close()
        conn.close()


    @staticmethod
    def record_employee_exit(documento_identidad, exit_time, motivo_retiro=None):
        employee_id = EmployeeService.find_employee_by_documento_identidad(documento_identidad)
        if employee_id is None:
            raise ValueError("Employee not found with the given documento_identidad.")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE employee_entries SET exit_time = %s, motivo_retiro = %s WHERE employee_id = %s AND exit_time IS NULL",
            (exit_time, motivo_retiro, employee_id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_entries_by_employee(employee_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM employee_entries WHERE employee_id = %s",
            (employee_id,)
        )
        entries = cursor.fetchall()
        cursor.close()
        conn.close()
        return entries

    @staticmethod
    def get_current_occupancy():
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query for current employees in the building
        cursor.execute(
            "SELECT COUNT(*) FROM employee_entries WHERE exit_time IS NULL"
        )
        employee_count = cursor.fetchone()[0]

        # Query for current guests in the building
        cursor.execute(
            "SELECT COUNT(*) FROM guest_entries WHERE exit_time IS NULL"
        )
        guest_count = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return employee_count + guest_count
