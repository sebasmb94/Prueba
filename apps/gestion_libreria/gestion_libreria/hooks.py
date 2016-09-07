# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "gestion_libreria"
app_title = "Gestion Libreria"
app_publisher = "ME"
app_description = "Aplicación para gestionar una libreria"
app_icon = "octicon octicon-book"
app_color = "#589494"
app_email = "me@eco.io"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gestion_libreria/css/gestion_libreria.css"
# app_include_js = "/assets/gestion_libreria/js/gestion_libreria.js"

# include js, css files in header of web template
# web_include_css = "/assets/gestion_libreria/css/gestion_libreria.css"
# web_include_js = "/assets/gestion_libreria/js/gestion_libreria.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "gestion_libreria.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "gestion_libreria.install.before_install"
# after_install = "gestion_libreria.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gestion_libreria.notifications.get_notification_config"

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
# 		"gestion_libreria.tasks.all"
# 	],
# 	"daily": [
# 		"gestion_libreria.tasks.daily"
# 	],
# 	"hourly": [
# 		"gestion_libreria.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gestion_libreria.tasks.weekly"
# 	]
# 	"monthly": [
# 		"gestion_libreria.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "gestion_libreria.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "gestion_libreria.event.get_events"
# }

