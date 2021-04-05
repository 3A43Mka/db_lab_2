from controller.UserController import UserController
from controller.AdminController import AdminController
from controller.Controller import Controller

menu_list = {
    'Main menu': {
        'Register': UserController.registration,
        'Sign in': UserController.sign_in,
        'Exit': Controller.stop_loop,
    },
    'User menu': {
        'Sign out': UserController.sign_out,
        'Send a message': UserController.send_message,
        'Inbox messages': UserController.inbox_message,
        'My messages statistics': UserController.get_message_statistics,
    },
    'Admin menu': {
        'Sign out': Controller.stop_loop,
        'Get logs': AdminController.get_events,
        'Online users': AdminController.get_online_users,
        'Most active senders': AdminController.get_top_senders,
        'Most active spamers': AdminController.get_top_spamers,
    }
}

roles = {
    'user': 'User menu',
    'admin': 'Admin menu'
}

special_parameters = {
    'role': '(admin or user)'
}
