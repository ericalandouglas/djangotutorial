from fabric.api import local

def backup():
	local('git pull origin master')
	local('git add .')
	print "Enter your commit comment:"
	comment = raw_input()
	local('git commit -m "%s"' % comment)
	local('git push origin master')

def switch_debug(what_to_change, change_to):
	local('cp djangotest1/local_settings.py djangotest1/local_settings.bak')
	sed = "sed 's/^DEBUG = %s$/DEBUG = %s/' djangotest1/local_settings.bak > djangotest1/local_settings.py"
	local(sed % (what_to_change, change_to))

def deploy():
	local('pip freeze > requirements.txt')
	backup()
	switch_debug('True', 'False')
	local('./manage.py collectstatic')
	switch_debug('False', 'True')
	local('heroku maintenance:on')
	local('git push heroku master')
	local('heroku run ./manage.py migrate')
	local('heroku maintenance:off')
