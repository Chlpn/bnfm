from odoo import fields, models, api, _
from openerp.exceptions import UserError


class AccountInvoice(models.Model):
   _inherit = "account.invoice"
   
   @api.model
   def action_cancel(self):
    if self.env['res.users'].has_group('account.group_account_manager'):
      rec= super(AccountInvoice, self).action_cancel()
    else:
      raise UserError(_('You are not privilaged to cancel this invoice'))
      rec=0   
       
    return rec
        
        
       
