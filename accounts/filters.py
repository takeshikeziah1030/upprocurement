import django_filters
from .models import Procurement


class ProcurementFilter(django_filters.FilterSet):
    class Meta:
        model = Procurement
        fields = ['Status', 'Types_of_Procurement', 'Start_Date']
        #exclude = ['PPMP_Attachment','PR_Attachment','PreBid_Attachment', 'Opening_Attachment',
        #            'PostQual_Attachment', 'NOA_Attachment', 'PO_Attachment', 'PO_Approved_attachment',
        #            'PO_Supplier_attachment','Delivery_Attachment','DVProcessing_Attachment','DVApproval_Attachment',
        #            'ORCR_Attachment','Checks_Attachment']