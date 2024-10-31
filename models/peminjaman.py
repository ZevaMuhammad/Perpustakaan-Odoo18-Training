from odoo import models, fields, api, exceptions

class Peminjaman(models.Model):
    _name = "peminjaman"
    _description = "Catatan Peminjaman"
    
    idp_buku = fields.Many2one("data.buku", string="Buku", required=True)
    idp_pengguna = fields.Many2one("res.users", string="User", required=True)
    tanggal_peminjaman = fields.Date(string="Tanggal Peminjaman", default=fields.Date.context_today, required=True)
    tanggal_pengembalian = fields.Date(string="Tanggal Pengembalian")
    status = fields.Selection(
        selection=[("dipinjam", "Dipinjam"),
                   ("dikembalikan", "Dikembalikan")],
        default="dipinjam",
        string="Status"
    )
    
    @api.model
    def borrow_buku(self, idp_pengguna, idp_buku):
        buku = self.env['data.buku'].browse(idp_buku)
        if buku.jumlah_copy < 1:
            raise exceptions.UserError("Tidak ada buku yang tersedia untuk dipinjam sekarang")
        buku.jumlah_copy -= 1
        return self.create({
            'idp_pengguna': idp_pengguna,
            'idp_buku': idp_buku,
            'tanggal_peminjaman': fields.Date.today(),
            'status': 'dipinjam'
        })

    def return_buku(self):
        for record in self:
            record.idp_buku.jumlah_copy += 1
            record.write({
                'tanggal_pengembalian': fields.Date.today(),
                'status': 'dikembalikan'
            })
