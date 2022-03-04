from copy import copy
from odoo import models, fields, api

class NcfTipo (models.Model):
    _name="vessla.ncf"
    _description ="Modelo tabla tipo de NCF"
    _rec_name="descripcion"

    tipo = fields.Char("Tipo", required=True, size=2, translate=True, copy=True)
    descripcion = fields.Char("Descripcion", required=True, translate=True, help="Indicar nombre del NCF")
    serie = fields.Char("Serie", required=True, translate=True)
    secuencial = fields.Integer("Secuencial", required=True, copy=True)

class NcfListado(models.Model):
    _name="vessla.ncf.lista"
    _description="Tabla listado de NCF"
    _rec_name="ncf_tipo_id"

    ncf_tipo_id = fields.Many2one("vessla.ncf", string="Tipo NCF", required=True, copy=False)
    # ncf_tipo_descripcion = fields.Char(string="descripcion", related='ncf_tipo_id.descripcion', tracking=True)
    desde = fields.Integer("Desde", required=True)
    hasta = fields.Integer("Hasta", required=True)
    proximo = fields.Integer("Proximo", required=True)
    fecha_vigencia = fields.Date(string="Valido hasta", required=True)

class SaleOrderInherited(models.Model):
    _inherit = 'sale.order' 
    custom_field = fields.Char(string='Custom Field')





