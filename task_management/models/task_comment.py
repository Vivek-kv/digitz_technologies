from odoo import models, fields, api
from odoo.exceptions import AccessError

class TaskComment(models.Model):
    _name = 'task.comment'
    _description = 'Task Comment'
    _order = 'creation_date desc'

    comment = fields.Text(string='Comment', required=True)
    task_id = fields.Many2one(
        'task.management', string='Task', required=True, ondelete='cascade')
    creation_date = fields.Datetime(
        string='Date', default=fields.Datetime.now)
    user_id = fields.Many2one(
        'res.users', string='User', default=lambda self: self.env.user)

