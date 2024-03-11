from odoo import models, fields, api


class TestModel(models.Model):
    _name = 'test_model'
    _description = 'Test Model'

    id = fields.Integer(string='ID', required=True)
    producto = fields.Char(string='Producto')
    viabilidad = fields.Float(string='Viabilidad')

    def create_five_products(self):
        products_data = [
            {'producto': 'Producto 1', 'viabilidad': 200.0},
            {'producto': 'Producto 2', 'viabilidad': 500.0},
            {'producto': 'Producto 3', 'viabilidad': 100.0},
            {'producto': 'Producto 4', 'viabilidad': 50.0},
            {'producto': 'Producto 5', 'viabilidad': 250.0},
        ]

        self.create(products_data)
        return True
