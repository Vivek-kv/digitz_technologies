{
    'name': 'Task Management',
    'version': '16.0.1.0.0',
    'summary': 'Manage tasks with API integration',
    'description': """
        Task Management System with mock API integration
        - Create and manage tasks
        - Add comments to tasks
        - Import tasks from external API
        - JSON endpoint for task data
    """,
    'category': 'Services/Task Management',
    'author': 'Vivek_KV',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'icon': '/task_management/static/description/odoo_icon.png',
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/task_management_views.xml',
        'views/task_management_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}