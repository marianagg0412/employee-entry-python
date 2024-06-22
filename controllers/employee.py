# controllers/employee.py
from flask import request, jsonify
from services.employee import EmployeeService

class EmployeeController:
    @staticmethod
    def register_employee():
        data = request.get_json()
        nombre = data['nombre']
        documento_identidad = data['documento_identidad']
        area = data['area']
        EmployeeService.register_employee(nombre, documento_identidad, area)
        return jsonify({"message": "Employee registered successfully"}), 201

    @staticmethod
    def get_employees():
        employees = EmployeeService.get_employees()
        return jsonify(employees)

    @staticmethod
    def get_employee_entries():
        employees = EmployeeService.get_employee_entries()
        return jsonify(employees)

    @staticmethod
    def employee_entry():
        data = request.get_json()
        documento_identidad = data['documento_identidad']
        entry_time = data['entry_time']
        EmployeeService.record_employee_entry(documento_identidad, entry_time)
        return jsonify({"message": "Entry recorded successfully"}), 201

    @staticmethod
    def employee_exit():
        data = request.get_json()
        documento_identidad = data['documento_identidad']
        exit_time = data['exit_time']
        motivo_retiro = data.get('motivo_retiro')
        EmployeeService.record_employee_exit(documento_identidad, exit_time, motivo_retiro)
        return jsonify({"message": "Exit recorded successfully"}), 201

    @staticmethod
    def get_entries_by_employee(employee_id):
        entries = EmployeeService.get_entries_by_employee(employee_id)
        return jsonify(entries)

    @staticmethod
    def get_current_occupancy():
        total_occupancy = EmployeeService.get_current_occupancy()
        return jsonify({"total_occupancy": total_occupancy})