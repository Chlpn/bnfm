from odoo import fields,models

class AccountInvoice(models.Model):
   _inherit = "account.invoice"
   
   @api.model
   def action_cancel(self):
    if self.env['res.users'].has_group('account.group_account_manager'):
      rec= return super(TransMaster, self).unlink()
    else:
      raise UserError(_('You are not privilaged to cancel this invoice'))
      rec=0   
       
    return rec
        
        
       