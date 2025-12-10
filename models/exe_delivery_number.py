# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = "stock.picking"

    delivery_number = fields.Char(string="Número de Remito", help="Número de Remito asociado a este albarán.", required=True)