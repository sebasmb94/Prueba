# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "management"
app_title = "Management"
app_publisher = "Me"
app_description = "organize books"
app_icon = "octicon octicon-book"
app_color = "#589494"
app_email = "me@er.io"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/management/css/management.css"
# app_include_js = "/assets/management/js/management.js"

# include js, css files in header of web template
# web_include_css = "/assets/management/css/management.css"
# web_include_js = "/assets/management/js/management.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "management.install.before_install"
# after_install = "management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"management.tasks.all"
# 	],
# 	"daily": [
# 		"management.tasks.daily"
# 	],
# 	"hourly": [
# 		"management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "management.event.get_events"
# }

