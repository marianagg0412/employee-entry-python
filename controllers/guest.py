from flask import request, jsonify
from services.guest import GuestService
from datetime import datetime

class GuestController:
    @staticmethod
    def register_guest():
        data = request.get_json()
        guest_name = data['guest_name']
        documento_identidad = data['documento_identidad']
        GuestService.register_guest(guest_name, documento_identidad)
        return jsonify({"message": "Guest registered successfully"}), 201

    @staticmethod
    def get_guests():
        guests = GuestService.get_guests()
        return jsonify(guests), 200
    
    @staticmethod
    def get_guest_entries():
        guests = GuestService.get_employee_entries()
        return jsonify(guests)

    @staticmethod
    def guest_entry():
        data = request.get_json()
        documento_identidad = data['documento_identidad']
        entry_time = datetime.now()
        GuestService.record_guest_entry(documento_identidad, entry_time)
        return jsonify({"message": "Entry recorded successfully"}), 201

    @staticmethod
    def guest_exit():
        data = request.get_json()
        documento_identidad = data['documento_identidad']
        exit_time = datetime.now()
        GuestService.record_guest_exit(documento_identidad, exit_time)
        return jsonify({"message": "Exit recorded successfully"}), 201

    @staticmethod
    def get_entries_by_guest(guest_id):
        entries = GuestService.get_entries_by_guest(guest_id)
        return jsonify(entries), 200
    
    @staticmethod
    def modify_guest(documento_identidad):
        data = request.get_json()
        new_guest_name = data.get('new_guest_name')
        new_guest_type = data.get('new_guest_type')
        GuestService.modify_guest(documento_identidad, new_guest_name, new_guest_type)
        return jsonify({"message": "Guest modified successfully"}), 200

    @staticmethod
    def delete_guest(documento_identidad):
        GuestService.delete_guest(documento_identidad)
        return jsonify({"message": "Guest deleted successfully"}), 200
