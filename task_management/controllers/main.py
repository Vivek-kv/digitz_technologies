from odoo import http
from odoo.http import request
import json


class TaskManagementController(http.Controller):

    @http.route('/task_management/tasks', type='http', auth='user', methods=['GET'])
    def get_tasks_json(self, **kwargs):
        try:
            tasks = request.env['task.management'].search([])
            task_list = []

            for task in tasks:
                task_list.append({
                    'name': task.name,
                    'description': task.description or '',
                    'priority': task.priority,
                    'status': task.status,
                    'assigned_user': task.assigned_user.name if task.assigned_user else '',
                    'due_date': task.due_date.strftime('%Y-%m-%d') if task.due_date else ''
                })

            return request.make_response(
                json.dumps(task_list),
                headers=[('Content-Type', 'application/json')]
            )
        except Exception as e:
            return request.make_response(
                json.dumps({'error': str(e)}),
                headers=[('Content-Type', 'application/json')],
                status=500
            )