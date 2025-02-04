from netbox.api.routers import NetBoxRouter

from . import views

app_name = 'netbox_contract'

router = NetBoxRouter()
router.register('contracts', views.ContractViewSet)
router.register('invoices', views.InvoiceViewSet)
router.register('contractassignment', views.ContractAssignmentViewSet)
router.register('invoiceline', views.InvoiceLineViewSet)
router.register('accountingdimension', views.AccountingDimensionViewSet)

urlpatterns = router.urls
