from circuits.models import Circuit
from dcim.models import Device, Site
from django.contrib.contenttypes.models import ContentType
from netbox.plugins import PluginTemplateExtension
from virtualization.models import VirtualMachine

from . import tables
from .models import AccountingDimension, Contract, ContractAssignment


class CircuitContractAssignments(PluginTemplateExtension):
    model = 'circuits.circuit'

    def full_width_page(self):
        circuit = self.context['object']
        circuit_type = ContentType.objects.get_for_model(Circuit)
        contract_assignments = ContractAssignment.objects.filter(content_type__pk=circuit_type.id, object_id=circuit.id)
        assignments_table = tables.ContractAssignmentObjectTable(contract_assignments)
        assignments_table.configure(self.context['request'])

        return self.render(
            'contract_assignments_bottom.html',
            extra_context={
                'assignments_table': assignments_table,
            },
        )


class DeviceContractAssignments(PluginTemplateExtension):
    model = 'dcim.device'

    def full_width_page(self):
        device = self.context['object']
        device_type = ContentType.objects.get_for_model(Device)
        contract_assignments = ContractAssignment.objects.filter(content_type__pk=device_type.id, object_id=device.id)
        assignments_table = tables.ContractAssignmentObjectTable(contract_assignments)
        assignments_table.configure(self.context['request'])

        return self.render(
            'contract_assignments_bottom.html',
            extra_context={
                'assignments_table': assignments_table,
            },
        )


class VMContractAssignments(PluginTemplateExtension):
    model = 'virtualization.virtualmachine'

    def full_width_page(self):
        vm = self.context['object']
        vm_type = ContentType.objects.get_for_model(VirtualMachine)
        contract_assignments = ContractAssignment.objects.filter(content_type__pk=vm_type.id, object_id=vm.id)
        assignments_table = tables.ContractAssignmentObjectTable(contract_assignments)
        assignments_table.configure(self.context['request'])

        return self.render(
            'contract_assignments_bottom.html',
            extra_context={
                'assignments_table': assignments_table,
            },
        )


class SiteContractAssignments(PluginTemplateExtension):
    model = 'dcim.site'

    def full_width_page(self):
        site = self.context['object']
        site_type = ContentType.objects.get_for_model(Site)
        contract_assignments = ContractAssignment.objects.filter(content_type__pk=site_type.id, object_id=site.id)
        assignments_table = tables.ContractAssignmentObjectTable(contract_assignments)
        assignments_table.configure(self.context['request'])

        return self.render(
            'contract_assignments_bottom.html',
            extra_context={
                'assignments_table': assignments_table,
            },
        )


class SiteAccountingCode(PluginTemplateExtension):
    models = ['dcim.site']

    def left_page(self):
        site = self.context['object']
        accounting_dimension = AccountingDimension.objects.filter(site=site)
        accounting_table = tables.AccountingDimensionListTable(accounting_dimension)

        return self.render(
            'accountingdimension_left.html',
            extra_context={
                'related_accounting_table': accounting_table,
            },
        )


class ProvidersContractList(PluginTemplateExtension):
    models = ['circuits.provider']

    def full_width_page(self):
        provider = self.context['object']
        contracts = Contract.objects.filter(provider=provider)
        contract_table = tables.ContractListTable(contracts)

        return self.render(
            'contract_list_bottom.html',
            extra_context={
                'contracts_table': contract_table,
            },
        )


template_extensions = [
    CircuitContractAssignments,
    DeviceContractAssignments,
    VMContractAssignments,
    SiteContractAssignments,
    SiteAccountingCode,
    ProvidersContractList,
]
