{
    'name': 'Exe Delivery Number',
    'version': '18.0',
    'category': 'Tools',
    'author':'Mauro Bogado,Exemax',
    'summary': 'Modulo para cargar el número de remito en las operaciones de inventario',
    'depends': ['base','sale', 'account', 'mail', 'stock'],
    'data': [
        'views/exe_delivery_number.xml',
        
    ],
    
    'installable': True,
    'application': False,
}   