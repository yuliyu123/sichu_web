# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table('cabinet_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('douban_id', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('cabinet', ['Book'])

        # Adding model 'BookComment'
        db.create_table('cabinet_bookcomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.Book'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('cabinet', ['BookComment'])

        # Adding model 'BookOwnership'
        db.create_table('cabinet_bookownership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.Book'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('has_ebook', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal('cabinet', ['BookOwnership'])

        # Adding model 'BookBorrowRecord'
        db.create_table('cabinet_bookborrowrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ownership', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.BookOwnership'])),
            ('borrower', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('borrow_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('planed_return_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('returned_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('cabinet', ['BookBorrowRecord'])

        # Adding model 'BookCabinet'
        db.create_table('cabinet_bookcabinet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('create_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal('cabinet', ['BookCabinet'])

        # Adding M2M table for field books on 'BookCabinet'
        db.create_table('cabinet_bookcabinet_books', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bookcabinet', models.ForeignKey(orm['cabinet.bookcabinet'], null=False)),
            ('bookownership', models.ForeignKey(orm['cabinet.bookownership'], null=False))
        ))
        db.create_unique('cabinet_bookcabinet_books', ['bookcabinet_id', 'bookownership_id'])

        # Adding model 'CabinetNews'
        db.create_table('cabinet_cabinetnews', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('lead', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('news', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('cabinet', ['CabinetNews'])

        # Adding model 'EBookRequest'
        db.create_table('cabinet_ebookrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('requester', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('bo_ship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.BookOwnership'])),
        ))
        db.send_create_signal('cabinet', ['EBookRequest'])

        # Adding model 'BookBorrowRequest'
        db.create_table('cabinet_bookborrowrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('requester', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('bo_ship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.BookOwnership'])),
            ('planed_return_date', self.gf('django.db.models.fields.DateField')()),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal('cabinet', ['BookBorrowRequest'])

        # Adding model 'Repository'
        db.create_table('cabinet_repository', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
        ))
        db.send_create_signal('cabinet', ['Repository'])

        # Adding M2M table for field admin on 'Repository'
        db.create_table('cabinet_repository_admin', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('repository', models.ForeignKey(orm['cabinet.repository'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('cabinet_repository_admin', ['repository_id', 'user_id'])

        # Adding M2M table for field members on 'Repository'
        db.create_table('cabinet_repository_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('repository', models.ForeignKey(orm['cabinet.repository'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('cabinet_repository_members', ['repository_id', 'user_id'])

        # Adding model 'JoinRepositoryRequest'
        db.create_table('cabinet_joinrepositoryrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('requester', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('repo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.Repository'])),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal('cabinet', ['JoinRepositoryRequest'])

        # Adding model 'Feedback'
        db.create_table('cabinet_feedback', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('cabinet', ['Feedback'])

        # Adding model 'Tag'
        db.create_table('cabinet_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal('cabinet', ['Tag'])

        # Adding model 'BookTagUse'
        db.create_table('cabinet_booktaguse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.Tag'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.Book'])),
        ))
        db.send_create_signal('cabinet', ['BookTagUse'])

        # Adding unique constraint on 'BookTagUse', fields ['tag', 'user', 'book']
        db.create_unique('cabinet_booktaguse', ['tag_id', 'user_id', 'book_id'])

        # Adding model 'BookOwnershipTagUse'
        db.create_table('cabinet_bookownershiptaguse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.Tag'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('bookown', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.BookOwnership'])),
        ))
        db.send_create_signal('cabinet', ['BookOwnershipTagUse'])

        # Adding model 'SysBookTagUse'
        db.create_table('cabinet_sysbooktaguse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.Tag'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cabinet.Book'])),
        ))
        db.send_create_signal('cabinet', ['SysBookTagUse'])


    def backwards(self, orm):
        # Removing unique constraint on 'BookTagUse', fields ['tag', 'user', 'book']
        db.delete_unique('cabinet_booktaguse', ['tag_id', 'user_id', 'book_id'])

        # Deleting model 'Book'
        db.delete_table('cabinet_book')

        # Deleting model 'BookComment'
        db.delete_table('cabinet_bookcomment')

        # Deleting model 'BookOwnership'
        db.delete_table('cabinet_bookownership')

        # Deleting model 'BookBorrowRecord'
        db.delete_table('cabinet_bookborrowrecord')

        # Deleting model 'BookCabinet'
        db.delete_table('cabinet_bookcabinet')

        # Removing M2M table for field books on 'BookCabinet'
        db.delete_table('cabinet_bookcabinet_books')

        # Deleting model 'CabinetNews'
        db.delete_table('cabinet_cabinetnews')

        # Deleting model 'EBookRequest'
        db.delete_table('cabinet_ebookrequest')

        # Deleting model 'BookBorrowRequest'
        db.delete_table('cabinet_bookborrowrequest')

        # Deleting model 'Repository'
        db.delete_table('cabinet_repository')

        # Removing M2M table for field admin on 'Repository'
        db.delete_table('cabinet_repository_admin')

        # Removing M2M table for field members on 'Repository'
        db.delete_table('cabinet_repository_members')

        # Deleting model 'JoinRepositoryRequest'
        db.delete_table('cabinet_joinrepositoryrequest')

        # Deleting model 'Feedback'
        db.delete_table('cabinet_feedback')

        # Deleting model 'Tag'
        db.delete_table('cabinet_tag')

        # Deleting model 'BookTagUse'
        db.delete_table('cabinet_booktaguse')

        # Deleting model 'BookOwnershipTagUse'
        db.delete_table('cabinet_bookownershiptaguse')

        # Deleting model 'SysBookTagUse'
        db.delete_table('cabinet_sysbooktaguse')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cabinet.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'douban_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cabinet.bookborrowrecord': {
            'Meta': {'object_name': 'BookBorrowRecord'},
            'borrow_date': ('django.db.models.fields.DateTimeField', [], {}),
            'borrower': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cabinet.BookOwnership']"}),
            'planed_return_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'returned_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'cabinet.bookborrowrequest': {
            'Meta': {'object_name': 'BookBorrowRequest'},
            'bo_ship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cabinet.BookOwnership']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'planed_return_date': ('django.db.models.fields.DateField', [], {}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'requester': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cabinet.bookcabinet': {
            'Meta': {'object_name': 'BookCabinet'},
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['cabinet.BookOwnership']", 'null': 'True', 'blank': 'True'}),
            'create_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        'cabinet.bookcomment': {
            'Meta': {'object_name': 'BookComment'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cabinet.Book']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cabinet.bookownership': {
            'Meta': {'object_name': 'BookOwnership'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cabinet.Book']"}),
            'has_ebook': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'cabinet.bookownershiptaguse': {
            'Meta': {'object_name': 'BookOwnershipTagUse'},
            'bookown': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cabinet.BookOwnership']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cabinet.Tag']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cabinet.booktaguse': {
            'Meta': {'unique_together': "(('tag', 'user', 'book'),)", 'object_name': 'BookTagUse'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cabinet.Book']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cabinet.Tag']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cabinet.cabinetnews': {
            'Meta': {'object_name': 'CabinetNews'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'news': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'cabinet.ebookrequest': {
            'Meta': {'object_name': 'EBookRequest'},
            'bo_ship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cabinet.BookOwnership']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requester': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cabinet.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cabinet.joinrepositoryrequest': {
            'Meta': {'object_name': 'JoinRepositoryRequest'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'repo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cabinet.Repository']"}),
            'requester': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'cabinet.repository': {
            'Meta': {'object_name': 'Repository'},
            'admin': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'managed_repos'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'joined_repos'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'cabinet.sysbooktaguse': {
            'Meta': {'object_name': 'SysBookTagUse'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cabinet.Book']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cabinet.Tag']"})
        },
        'cabinet.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cabinet']