import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .models import (
    AccountingDimension,
    Contract,
    ContractAssignment,
    Invoice,
    InvoiceLine,
)


class ContractAssignmentListTable(NetBoxTable):
    content_type = columns.ContentTypeColumn(verbose_name='Object Type')
    content_object = tables.Column(linkify=True, orderable=False)
    contract = tables.Column(linkify=True)
    actions = columns.ActionsColumn(actions=('edit', 'delete'))
    contract__provider = tables.Column(linkify=True)
    contract__accounting_code = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = ContractAssignment
        fields = (
            'pk',
            'content_type',
            'content_object',
            'contract',
            'contract__provider',
            'contract__accounting_code',
            'actions',
        )
        default_columns = (
            'pk',
            'content_type',
            'content_object',
            'contract',
            'contract__provider',
            'contract__accounting_code',
        )


class ContractAssignmentObjectTable(NetBoxTable):
    contract = tables.Column(linkify=True)
    actions = columns.ActionsColumn(actions=('edit', 'delete'))
    contract__provider = tables.Column(verbose_name='Partner', linkify=True)
    contract__accounting_code = tables.Column(verbose_name=('Accounting Code'), linkify=True)
    contract__status = columns.ChoiceFieldColumn(
        verbose_name=('Status'),
    )

    class Meta(NetBoxTable.Meta):
        model = ContractAssignment
        fields = (
            'pk',
            'contract',
            'contract__provider',
            'contract__accounting_code',
            'contract__status',
            'contract__start_date',
            'contract__end_date',
            'contract__mrc',
            'contract__nrc',
            'actions',
        )
        default_columns = (
            'pk',
            'contract',
            'contract__provider',
            'contract__accounting_code',
            'contract__status',
            'contract__start_date',
            'contract__end_date',
            'contract__mrc',
            'contract__nrc',
        )


class ContractAssignmentContractTable(NetBoxTable):
    content_type = columns.ContentTypeColumn(verbose_name='Object Type')
    content_object = tables.Column(linkify=True, verbose_name='Object', orderable=False)
    content_object__status = columns.ChoiceFieldColumn(
        verbose_name=('Status'),
    )
    actions = columns.ActionsColumn(actions=('edit', 'delete'))

    class Meta(NetBoxTable.Meta):
        model = ContractAssignment
        fields = (
            'pk',
            'content_type',
            'content_object',
            'content_object__status',
            'actions',
        )
        default_columns = (
            'pk',
            'content_type',
            'content_object',
            'content_object__status',
        )


class ContractListTable(NetBoxTable):
    name = tables.Column(linkify=True)
    accounting_code = tables.Column(verbose_name='Accounting Code', linkify=True)
    provider = tables.Column(verbose_name='Provider', linkify=True)
    parent = tables.Column(linkify=True)
    yrc = tables.Column(verbose_name='Yerly recuring costs')
    status = columns.ChoiceFieldColumn(
        verbose_name=('Status'),
    )

    class Meta(NetBoxTable.Meta):
        model = Contract
        fields = (
            'pk',
            'id',
            'name',
            'accounting_code',
            'provider',
            'external_reference',
            'status',
            'start_date',
            'end_date',
            'initial_term',
            'renewal_term',
            'mrc',
            'yrc',
            'nrc',
            'invoice_frequency',
            'documents',
            'comments',
            'parent',
            'actions',
        )
        default_columns = ('name', 'provider', 'accounting_code', 'status', 'parent')


class ContractListBottomTable(NetBoxTable):
    name = tables.Column(linkify=True)
    accounting_code = tables.Column(verbose_name='Accounting Code', linkify=True)
    provider = tables.Column(linkify=True)
    status = columns.ChoiceFieldColumn(
        verbose_name=('Status'),
    )

    class Meta(NetBoxTable.Meta):
        model = Contract
        fields = (
            'pk',
            'id',
            'name',
            'accounting_code',
            'provider',
            'external_reference',
            'status',
            'mrc',
            'comments',
            'actions',
        )
        default_columns = (
            'name',
            'accounting_code',
            'provider',
            'status',
        )


class InvoiceListTable(NetBoxTable):
    contracts = tables.ManyToManyColumn(linkify=True)
    number = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = Invoice
        fields = (
            'pk',
            'id',
            'number',
            'date',
            'contracts',
            'period_start',
            'period_end',
            'amount',
            'documents',
            'comments',
            'actions',
        )
        default_columns = (
            'number',
            'date',
            'contracts',
            'period_start',
            'period_end',
            'amount',
        )


class InvoiceLineListTable(NetBoxTable):
    invoice = tables.Column(linkify=True)
    accounting_dimensions = tables.ManyToManyColumn(linkify=True, filter=lambda qs: qs.order_by('name'))

    class Meta(NetBoxTable.Meta):
        model = InvoiceLine
        fields = (
            'pk',
            'invoice',
            'amount',
            'accounting_dimensions',
            'comments',
        )
        default_columns = (
            'pk',
            'invoice',
            'amount',
            'currency',
            'accounting_dimensions',
            'comments',
        )


class AccountingDimensionListTable(NetBoxTable):
    status = columns.ChoiceFieldColumn(
        verbose_name=('Status'),
    )

    class Meta(NetBoxTable.Meta):
        model = AccountingDimension
        fields = (
            'pk',
            'name',
            'value',
            'site',
            'comments',
            'status',
        )
        default_columns = (
            'name',
            'value',
            'site',
            'comments',
            'status',
        )
