from fabric.api import env, run, cd

USERNAME = 'root'
SERVER = 'zsu.mydomain.com'
APP_NAME = 'carwasher'
PROJECT_DIR = '/var/www/wsgi_apps/%s' % (APP_NAME)
WSGI_SCRIPT = '../carwasher.wsgi'

env.hosts = ["%s@%s" % (USERNAME, SERVER)]
env.password = 'Su650302'

def deploy():
    with cd(PROJECT_DIR):
        run('git pull')
        run('source venv/bin/activate; pip install -r requirements.txt')
        run('touch %s' % WSGI_SCRIPT)
