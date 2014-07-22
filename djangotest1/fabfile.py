from fabric.api import local

def backup():
	local('git pull origin master')
	local('git add .')
	print "Enter your commit comment:"
	comment = raw_input()
	local('git commit -m "%s"' % comment)
	lcoal('git push origin master')