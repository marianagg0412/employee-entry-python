from flask import Blueprint
from controllers.employee import EmployeeController

employee_bp = Blueprint('employee_bp', __name__)

employee_bp.route('/register_employee', methods=['POST'])(EmployeeController.register_employee)
employee_bp.route('/employees', methods=['GET'])(EmployeeController.get_employees)
employee_bp.route('/employee_all', methods=['GET'])(EmployeeController.get_employee_entries)
employee_bp.route('/employee_entry', methods=['POST'])(EmployeeController.employee_entry)
employee_bp.route('/employee_exit', methods=['POST'])(EmployeeController.employee_exit)
employee_bp.route('/employee_entries/<int:employee_id>', methods=['GET'])(EmployeeController.get_entries_by_employee)
employee_bp.route('/current_occupancy', methods=['GET'])(EmployeeController.get_current_occupancy)