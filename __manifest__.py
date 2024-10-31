{
    'name': "Perpustakaan Sekolah",
    'version': '1.0',
    'depends': ['base'],
    'author': "Zeva Muhammad",
    'category': 'App',
    'description': """
        Latihan Pembutan Applikasi Di Odoo 18 
    """,
    'application': True,

    'data': [
        'security/ir.model.access.csv',    
        'views/menu.xml',
        'views/menu_peminjaman.xml',
    ]
}