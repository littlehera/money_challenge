# -*- coding: utf-8 -*-
# Copyright (c) 2018, littlehera and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, datetime
from frappe.model.document import Document

class Challenge(Document):
	pass
@frappe.whitelist()
def generate_weekly_cycles(challenge_scheme, amount, generated_iterations):
	increment = 0
	# if cycles haven't been generated yet, create cycles. Don't create 52 week cycles if they already exist.
	print generated_iterations
	if int(generated_iterations) == 0:
		print "whut"
		if challenge_scheme == "Same Amount Each Week":
			increment = 0
		else:
			increment = float(amount)
		weekly_cycles = get_weekly_cycles(increment, float(amount))
		return weekly_cycles
	else:
		pass

def get_weekly_cycles(increment, amount):
	cycles = []
	from_date = (datetime.date.today().replace(day=1))
	i = 0
	while i<52:
		if increment == 0:
			pass
		else:
			if i!= 0:
				amount += increment
		end_date = from_date + datetime.timedelta(days=7)
		week = ""+from_date.strftime("%b-%d")+" - "+end_date.strftime("%b-%d")
		#print week, amount
		cycle = {"week":week,
				 "amount":amount,
				 "from_date":from_date,
				 "end_date":end_date}
		cycles.append(cycle)
		from_date = end_date
		i+=1
	print len(cycles)
	return cycles

def get_year():
	return datetime.date.today().year