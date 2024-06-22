from flask import Blueprint
from controllers.guest import GuestController

guest_bp = Blueprint('guest_bp', __name__)

guest_bp.route('/register_guest', methods=['POST'])(GuestController.register_guest)
guest_bp.route('/guests', methods=['GET'])(GuestController.get_guests)
guest_bp.route('/guests_all', methods=['GET'])(GuestController.get_guest_entries)
guest_bp.route('/guest_entry', methods=['POST'])(GuestController.guest_entry)
guest_bp.route('/guest_exit', methods=['POST'])(GuestController.guest_exit)
guest_bp.route('/guest_entries/<int:guest_id>', methods=['GET'])(GuestController.get_entries_by_guest)
guest_bp.route('/modify_guest/<string:documento_identidad>', methods=['PUT'])(GuestController.modify_guest)
guest_bp.route('/delete_guest/<string:documento_identidad>', methods=['DELETE'])(GuestController.delete_guest)