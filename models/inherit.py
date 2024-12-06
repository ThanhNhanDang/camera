from odoo import models, api, tools, fields, _
import psycopg2
from odoo.exceptions import UserError
import logging  # Nhập thư viện logging để ghi lại thông tin và lỗi
_logger = logging.getLogger(__name__)  # Tạo logger để ghi lại thông tin


class Inherit(models.Model):
    _inherit = 'res.partner'

    camera_open = fields.Boolean(string="Chụp hình")
    image_1920_1 = fields.Image(string="Ảnh Trên",
                                max_width=1920, max_height=1920)
    image_1920_2 = fields.Image(string="Ảnh Dưới",
                                max_width=1920, max_height=1920)
    image_1920_3 = fields.Image(string="Ảnh Trái",
                                max_width=1920, max_height=1920)
    image_1920_4 = fields.Image(string="Ảnh Phải",
                                max_width=1920, max_height=1920)
