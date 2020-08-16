# -*- coding: utf-8 -*-
# Copyright (c) 2020, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Meeting(Document):
    def validate(self):
        for attendee in self.attendees:
            if attendee.full_name is None:
                attendee.full_name = get_full_name(attendee.attendee_user)

@frappe.whitelist()
def get_full_name(attendee):
    user = frappe.get_doc("User", attendee)
    return user.full_name
