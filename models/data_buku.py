from odoo import models, fields, api, exceptions
from datetime import datetime

class DataBuku(models.Model):
    _name = "data.buku"
    _description = "Data Buku"
    
    id_buku = fields.Char(string="Id Buku", required=True)
    judul = fields.Char(string="Judul Buku", required=True)
    penerbit = fields.Char(string="Nama Penerbit", required=True)
    tanggal_terbit = fields.Date(string="Tanggal Terbit", required=True)
    genre = fields.Selection(
        selection=[
            ("fiksi", "Fiksi"),
            ("non-fiksi", "Non - Fiksi"),
            ("edukasi", "Edukasi"),
            ("buku-anak-anak", "Buku Anak-anak"),
            ("biologi", "Biologi"),
        ],
        string="Genre Buku",
        required=True
    )
    lokasi = fields.Selection(
        selection=[
            ("a1", "A1"),
            ("a2", "A2"),
            ("b1", "B1"),
            ("b2", "B2"),
            ("c1", "C1"),
            ("c2", "C2"),
            ("d1", "D1"),
            ("d2", "D2"),
        ],
        string="Letak Buku Pada Rak",
        required=True
    )
    jumlah_copy = fields.Integer(string="Jumlah Copy", required=True, default=1)
    deskripsi = fields.Text(string="Deskripsi Singkat", required=True)
    tahun_penerbitan = fields.Char(string="Tahun Penerbitan", compute="_compute_tahun_penerbitan")
    status = fields.Selection(
        selection=[("dipinjam", "Dipinjam"),
                   ("dikembalikan", "Dikembalikan")],
        default="dipinjam",
        string="Status"
    )

    @api.depends('tanggal_terbit')
    def _compute_tahun_penerbitan(self):
        for record in self:
            if record.tanggal_terbit:
                record.tahun_penerbitan = record.tanggal_terbit.strftime('%Y')
            else:
                record.tahun_penerbitan = ''

    def action_pinjam_buku(self):
        for record in self:
            if record.jumlah_copy <= 0:
                raise exceptions.UserError("No copies available to borrow.")
            
            borrowing_record = self.env['peminjaman'].create({
                'idp_pengguna': self.env.uid,
                'idp_buku': record.id,
                'tanggal_peminjaman': datetime.today(),
            })
            
            record.jumlah_copy -= 1
            return borrowing_record