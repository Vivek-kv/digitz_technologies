from odoo import models, fields, api, _
from odoo.exceptions import UserError
import requests
import logging

_logger = logging.getLogger(__name__)


class TaskManagement(models.Model):
    _name = 'task.management'
    _description = 'Task Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority, due_date'

    name = fields.Char(string='Task Name', tracking=True)
    description = fields.Text(string='Description', tracking=True)
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Medium'), ('3', 'High')], string='Priority', help="Priority", default='0')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='Status', default='draft', tracking=True)
    assigned_user = fields.Many2one(
        'res.users', string='Assigned User', tracking=True)
    due_date = fields.Date(string='Due Date', tracking=True)
    comment_ids = fields.One2many(
        'task.comment', 'task_id', string='Comments')

    @api.model
    def get_view(self, view_id=None, view_type='form', **kwargs):
        res = super(TaskManagement, self).get_view(view_id=view_id, view_type=view_type, **kwargs)

        if not self.env.user.has_group('task_management.group_task_manager'):
            if view_type in ['form', 'tree', 'kanban']:
                from lxml import etree
                import json
                doc = etree.XML(res['arch'])

                for node in doc.xpath(
                        "//field[not(ancestor::field[@name='comment_ids']) and not(@name='comment_ids')]"):
                    node.set('readonly', '1')
                    modifiers = json.loads(node.get("modifiers", '{}'))
                    modifiers['readonly'] = True
                    node.set("modifiers", json.dumps(modifiers))

                for tree in doc.xpath("//field[@name='comment_ids']/tree"):
                    tree.set('delete', 'false')
                    modifiers = json.loads(tree.get("modifiers", '{}'))
                    modifiers['delete'] = False
                    tree.set("modifiers", json.dumps(modifiers))

                res['arch'] = etree.tostring(doc, encoding='unicode')
        return res

    def import_tasks_from_api(self):
        try:
            response = requests.get(
                'https://jsonplaceholder.typicode.com/todos', timeout=10)
            response.raise_for_status()
            tasks_data = response.json()

            created_count = 0
            for task_data in tasks_data:
                existing_task = self.search(
                    [('name', '=', task_data.get('title'))], limit=1)
                if not existing_task:
                    self.create({
                        'name': task_data.get('title'),
                        'description': f"Imported from API. User ID: {task_data.get('id')}",
                        'status': 'done' if task_data.get('completed') else 'draft',
                        'priority': '2',
                    })
                    created_count += 1

            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': f"Successfully imported {created_count} tasks!",
                    'type': 'rainbow_man',
                }
            }
        except requests.exceptions.RequestException as e:
            _logger.error("Error importing tasks: %s", e)
            raise UserError(_("Error connecting to API: %s") % e)
        except Exception as e:
            _logger.error("Error processing API data: %s", e)
            raise UserError(_("Error processing API data: %s") % e)