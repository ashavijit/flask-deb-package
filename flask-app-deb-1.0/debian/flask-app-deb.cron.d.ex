#
# Regular cron jobs for the flask-app-deb package
#
0 4	* * *	root	[ -x /usr/bin/flask-app-deb_maintenance ] && /usr/bin/flask-app-deb_maintenance
