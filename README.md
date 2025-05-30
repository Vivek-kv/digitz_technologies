# digitz_technologies
### Task Management System for Odoo 16

### Overview

This Odoo module provides a comprehensive task management system with API integration capabilities. It allows users to create, track, and manage tasks with features like comments, priority levels, status tracking, and due dates. The module also includes functionality to import tasks from an external API and provides a JSON endpoint to access task data.
Features

    Task creation and management

    Priority levels (Very Low to High)

    Status tracking (Draft, In Progress, Done)

    User assignment and due dates

    Comments system for each task

    API integration to import tasks from jsonplaceholder.typicode.com

    JSON endpoint to access task data

    Kanban, tree, and form views

    Access control with Task Manager group

### Installation

1. Clone or download this module into your Odoo addons directory:

    ```bash
    git clone https://github.com/Vivek-kv/digitz_technologies.git
    ```

2. Restart the Odoo server:

    ```bash
    ./odoo-bin -u task_management
    ```

    Or from within the Odoo UI, go to **Apps > Update Apps List**, then search for **Task Management** and install it.

3. Once installed, navigate to the **Task Management** menu to start managing tasks.


### Configuration

    User Groups:

        The module creates a "Task Manager" group with full access. assign this group as shown below
        Go to Settings → Users and Companies → Users → Task Management

        Regular users will have read-only access to tasks but can add comments

    Menu Access:

        The main menu is located under "Task Management" → "Tasks"

### Usage
Creating and Managing Tasks

    Navigate to "Task Management" → "Tasks"

    Click "Create" to add a new task

    Fill in the task details:

        Name

        Description

        Priority

        Status

        Assigned User

        Due Date

Adding Comments

    Open a task in form view

    Go to the "Comments" tab

    Click "Add a line" to add a new comment

    Enter your comment and save

### Search, Filter, Group By

    - Custom model: `task.management`
      - Search view with the following capabilities:
        - Search by Task Name and Assigned User
        - Filter by:
          - High Priority Tasks
          - Overdue Tasks (due date earlier than today)
        - Group by:
          - Status
          - Priority

Importing Tasks from API

    Only available for users in the "Task Manager" group

    Click the "Import Tasks" button in the task form view

    The system will fetch tasks from jsonplaceholder.typicode.com/todos

    Successfully imported tasks will appear in your task list

Accessing Task Data via API

    The module provides a JSON endpoint at /task_management/tasks

    Authenticated users can access this endpoint to get task data in JSON format

Security

    Regular users can view tasks but cannot modify them (except for adding comments)

    Only users in the "Task Manager" group can:

        Create, edit, and delete tasks

        Import tasks from the external API

        Delete comments

### Technical Details

    Task model: task.management

    Comments model: task.comment

    Dependencies: base, mail

    Views: Kanban, tree, form, and search views

    Controller: Provides JSON endpoint for task data

### Troubleshooting

    If API import fails, check the server logs for details

    Ensure users have proper group assignments to access all features

    The external API might have rate limits - if imports fail, try again later

### License

This module is licensed under LGPL-3.
### Author

### Vivek KV
