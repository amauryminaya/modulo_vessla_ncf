from odoo import models, fields

class NcfTipo (models.Model):
    _name="vessla.ncf"
    _description ="Modelo tabla tipo de NCF"
    _rec_name="descripcion"

    tipo = fields.Char("Tipo", required=True, size=2, translate=True)
    descripcion = fields.Char("Descripcion", required=True, translate=True)
    serie = fields.Char("Serie", required=True, translate=True)
    secuencial = fields.Integer("Secuencial", required=True)

class NcfListado(models.Model):
    _name="vessla.ncf.lista"
    _description="Tabla listado de NCF"
    _rec_name="ncf_tipo_id"

    ncf_tipo_id = fields.Many2one("vessla.ncf", string="Tipo NCF")
    # ncf_tipo_descripcion = fields.Char(string="descripcion", related='ncf_tipo_id.descripcion', tracking=True)
    
    desde = fields.Integer("Desde")
    hasta = fields.Integer("Hasta")
    proximo = fields.Integer("Proximo")
    fecha_vigencia = fields.Date(string="Valido hasta")


    
# @api.multi
# @api.depends("origin")
# def _compute_order_id(self):
#     for invoice in self:
#          order_ids = self.env["sale.order"].search([("name","=",invoice.origin)])
#          if len(order_ids) > 0:
#              invoice.order_id = order_ids[0]
# order_id = fields.Many2one("sale.order",compute=_compute_order_id, store=True) 





