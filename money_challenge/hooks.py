# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "money_challenge"
app_title = "Money Challenge App"
app_publisher = "littlehera"
app_description = "The 52 Week Money Challenge App with Email Reminders"
app_icon = "octicon octicon-law"
app_color = "green"
app_email = "villanuevahera@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/money_challenge/css/money_challenge.css"
# app_include_js = "/assets/money_challenge/js/money_challenge.js"

# include js, css files in header of web template
# web_include_css = "/assets/money_challenge/css/money_challenge.css"
# web_include_js = "/assets/money_challenge/js/money_challenge.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "money_challenge.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "money_challenge.install.before_install"
# after_install = "money_challenge.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "money_challenge.notifications.get_notification_config"

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
# 		"money_challenge.tasks.all"
# 	],
# 	"daily": [
# 		"money_challenge.tasks.daily"
# 	],
# 	"hourly": [
# 		"money_challenge.tasks.hourly"
# 	],
# 	"weekly": [
# 		"money_challenge.tasks.weekly"
# 	]
# 	"monthly": [
# 		"money_challenge.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "money_challenge.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "money_challenge.event.get_events"
# }

