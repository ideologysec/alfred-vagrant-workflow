from subprocess import call

# TODO: handle possible failiure of osascript

# Dict contains all Vagrant actions this workflow supports and metadata:
# ---
# 'desc': description field showed in alfred
# 'flags': additional command line flags for vagrant command
# 'state': machine state for which this action needs to be showed
# 'dir_action': flag to mark if action is possible on entire vagrant dir
actions = {
    'up': {
        'desc': 'Starts and provisions the vagrant environment',
        'flags': None,
        'state': ['paused', 'stopped'],
        'dir_action': True,
    },
    'halt': {
        'desc': 'Stops the machine',
        'flags': None,
        'state': ['running', 'paused'],
        'dir_action': True,
    },
    'resume': {
        'desc': 'Resume a suspended machine',
        'flags': None,
        'state': ['paused'],
        'dir_action': True,
    },
    'suspend': {
        'desc': 'Suspends the machine',
        'flags': None,
        'state': ['running'],
        'dir_action': True,
    },
    'provision': {
        'desc': 'Provisions the machine',
        'flags': None,
        'state': ['running'],
        'dir_action': True,
    },
    'rdp': {
        'desc': 'Connects to machine via RDP',
        'flags': None,
        'state': ['running'],
        'dir_action': False,
    },
    'ssh': {
        'desc': 'Connects to machine via SSH',
        'flags': None,
        'state': ['running'],
        'dir_action': False,
    },
    'destroy': {
        'desc': 'Stops and deletes all traces of the machine',
        'flags': '-f',
        'state': ['running', 'paused', 'stopped'],
        'dir_action': True,
    }
}


def send_notification(msg):
    call(['osascript', '-e',
          'tell application "Alfred 2" to run trigger "send_notification" '
          'in workflow "com.sverdlik.michael" '
          'with argument "{}"'.format(msg)])


def run_alfred(action):
    """Launch Alfred 2 via AppleScript and search for 'action'"""
    call(['osascript', '-e',
          'tell application "Alfred 2" to search "{}"'.format(action)])