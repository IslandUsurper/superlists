import subprocess

from os import path
THIS_FOLDER = path.dirname(path.abspath(__file__))

SSH_HOST = '192.168.1.74'

def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            'fab',
            'create_session_on_server:site_name={},email={}'.format(host, email),
            '--hosts={}'.format(SSH_HOST),
            '--hide=everything,status',
        ],
        cwd=THIS_FOLDER
    ).decode().strip()

def reset_database(host):
    subprocess.check_call(
        ['fab', 'reset_database:site_name={}', '--hosts={}'.format(host, SSH_HOST)],
        cwd=THIS_FOLDER
    )
