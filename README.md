Perpustakaan - Odoo Library Management System (Training Project)
Welcome to the Perpustakaan module, an Odoo library management system developed as a training project. This module serves as a comprehensive, hands-on exercise in Odoo development, covering key concepts like model definitions, view customizations, user access control, and business logic through custom methods. This repository is intended solely for personal training and learning purposes and is not intended for production use.

Purpose
The purpose of this module is to practice and gain familiarity with Odoo development essentials, including:

Defining custom models and fields.
Creating and modifying views, such as forms, lists, and search views.
Setting up access rights and record rules.
Implementing custom business logic with Python methods.
Utilizing XML for configurations and data structure.
Module Structure
This module, Perpustakaan, contains the following key components:

1. Models
Data Buku (data.buku): This model manages book records, tracking details such as id_buku (Book ID), judul (Title), penerbit (Publisher), tanggal_terbit (Publication Date), genre (Genre), lokasi (Location), jumlah_copy (Number of Copies), and deskripsi (Description).
Peminjaman (peminjaman): A borrowing record that logs book loans, including details about the borrowed book and the user.
2. Views
List View for data.buku: Displays a table of available books, showing essential information.
Form View for data.buku: A detailed view where users can see and edit book information. Includes a "Borrow" button, which triggers the borrowing process.
Search View for data.buku: Allows users to search for books by fields like id_buku, judul, and penerbit, and filter by genre.
List and Form Views for peminjaman: Manages records of book loans, showing borrowed book details and borrower information.
3. Access Control
ir.model.access.csv: Configures access rights for each model in the module. This file defines permissions for reading, writing, creating, and deleting records within data.buku and peminjaman.
4. Business Logic
Custom Borrowing Function: In the data_buku model, the action_pinjam_buku method creates a peminjaman record, storing a reference to the book and user. This feature demonstrates Odoo's ORM capabilities and custom method implementation.
Installation
To use this module, install it within an Odoo development environment set up for training. Clone this repository, place the module within your Odoo add-ons directory, and restart the Odoo server. Once Odoo recognizes the module, install it from the Apps menu.

Usage
After installation, navigate to the Perpustakaan menu. Here you can:

Manage Books: Add, view, or edit books.
Borrow Books: Use the "Borrow" button within book records to create borrowing entries, simulating a library lending process.
View Borrowing Records: Access and manage borrowing entries in the Catatan Peminjaman section.
Access Control Details
To ensure controlled access, access rights are set as follows:

Data Buku (data.buku): All basic user permissions (read, write, create, delete) are granted.
Peminjaman (peminjaman): Permissions are limited based on the role and purpose of the user.
License
This project is a personal training exercise and is not intended for commercial or production use.

