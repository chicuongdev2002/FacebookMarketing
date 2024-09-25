from odoo import models, fields, api
from datetime import timedelta
import logging
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)
class AutoCommentSchedule(models.Model):
    _name = 'auto.comment.schedule'
    _description = 'Auto Comment Schedule'

    post_id = fields.Many2one('marketing.post', string='Post ID', required=True, ondelete='cascade')
    end_time = fields.Datetime(string='End Time', required=True)
    remind_time_id = fields.Many2one('custom.remind.time', string='Remind Time')
    reminder_next_time = fields.Datetime(string='Next Reminder Time')
