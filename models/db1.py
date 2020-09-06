# -*- coding: utf-8 -*-

# pages categories
db.define_table('cat',
    Field('name'),
    Field('folder', length=30, comment='folder path (directory)'),
    format='%(name)s'
    )

# pages
db.define_table('pg',
    Field('cat_id', db.cat),
    Field('dte', 'date', default=request.now ),
    Field('arg', length=30, comment='argument for file name', unique = False), # cat+arg - unique
    Field('name'),
    Field('vip', 'integer', default=0),
    #Field('as_file', 'boolean', comment='if as view file - no in DB'),
    Field('descr', 'text', widget=ckeditor.widget),
    Field('see', 'integer', default=0, comment='просмотров'),
    Field('lke', 'integer', default=0, comment='понравилось'),
    )
