from django.db import models
from datetime import datetime, date
from django.urls import reverse
# Create your models here.

class Procurement(models.Model):
    choices = (
        ('New_Request', 'New_Request'),
        ('Resubmission', 'Resubmission'),
        ('On-Going', 'On-Going'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
        
    )

    locations = (
        ('End-User', 'End-User'),
        ('Procurement-Office', 'Procurement-Office'),
        ('Accounting-Office', 'Accounting-Office'),
        ('ADRIDE', 'ADRIDE'),
        ('SPMO', 'SPMO'),
        ('Supplier', 'Supplier'),
        ('Cashier-Office', 'Cashier-Office'),
    )

    Types = (
        ('Repeat-Order', 'Repeat-Order'),
        ('Direct-Contracting', 'Direct-Contracting'),
        ('Shopping/Small-Value-Procurement/Lease-of-Venue', 'Shopping/Small-Value-Procurement/Lease-of-Venue'),
        ('Special-Procurement', 'Special-Procurement'),
        ('Purchase-Order', 'Purchase-Order'),
        ('Bidding-Less-Than-1M', 'Bidding-Less-Than-1M'),
        ('Bidding-1M-and-Above', 'Bidding-1M-and-Above'),
    )
    Equipment = models.CharField(max_length=150, blank=True, null=True)
    PONo = models.CharField(max_length=150, blank=True, null=True)
    Delivery_Terms = models.CharField(max_length=150, blank=True, null=True)
    Budget = models.CharField(max_length=150, blank=True, null=True)
    PPMP_Date = models.CharField(max_length=150, blank=True, null=True)
    PPMP_Signatures = models.CharField(max_length=150, blank=True, null=True)
    PPMP_Pages = models.CharField(max_length=150, blank=True, null=True)
    PPMP_Days = models.CharField(max_length=150, blank=True, null=True)
    Requested_By = models.CharField(max_length=150, blank=True, null=True)
    Requested_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    Requested_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    PPMP_Attachment = models.FileField(upload_to='documents/PPMP/', blank=True, null=True)
    Types_of_Procurement = models.CharField(max_length=100, choices=Types, default="Purchase-Order")

    
    PR_Date = models.CharField(max_length=150, blank=True, null=True)
    PR_Signatures = models.CharField(max_length=150, blank=True, null=True)
    PR_Pages = models.CharField(max_length=150, blank=True, null=True)
    PR_Days = models.CharField(max_length=150, blank=True, null=True)
    PR_Rejected_By = models.CharField(max_length=150, blank=True, null=True)
    PR_Approved_By = models.CharField(max_length=150, blank=True, null=True)
    PR_Approved_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    PR_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    PR_Attachment = models.FileField(upload_to='documents/PR/', blank=True, null=True)

    Pre_Bid_Date = models.CharField(max_length=150, blank=True, null=True)
    Pre_Bid_Signatures = models.CharField(max_length=150, blank=True, null=True)
    Pre_Bid_Pages = models.CharField(max_length=150, blank=True, null=True)
    Pre_Bid_Days = models.CharField(max_length=150, blank=True, null=True)
    PreBid_Approved_By = models.CharField(max_length=150, blank=True, null=True)
    PreBid_Approved_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    PreBid_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    PreBid_Attachment = models.FileField(upload_to='documents/PreBids/', blank=True, null=True)

    Opening_Bid_Date = models.CharField(max_length=150, blank=True, null=True)
    Opening_Bid_Signatures = models.CharField(max_length=150, blank=True, null=True)
    Opening_Bid_Pages = models.CharField(max_length=150, blank=True, null=True)
    Opening_Bid_Days = models.CharField(max_length=150, blank=True, null=True)
    OpeningBid_Approved_By = models.CharField(max_length=150, blank=True, null=True)
    OpeningBid_Approved_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    Opening_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    Opening_Attachment = models.FileField(upload_to='documents/Opening/', blank=True, null=True)

    Post_Qual_Date = models.CharField(max_length=150, blank=True, null=True)
    Post_Qual_Signatures = models.CharField(max_length=150, blank=True, null=True)
    Post_Qual_Pages = models.CharField(max_length=150, blank=True, null=True)
    Post_Qual_Days = models.CharField(max_length=150, blank=True, null=True)
    PostQual_Approved_By = models.CharField(max_length=150, blank=True, null=True)
    PostQual_Approved_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    PostQual_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    PostQual_Attachment = models.FileField(upload_to='documents/Post/', blank=True, null=True)

    NOA_Date = models.CharField(max_length=150, blank=True, null=True)
    NOA_Signatures = models.CharField(max_length=150, blank=True, null=True)
    NOA_Pages = models.CharField(max_length=150, blank=True, null=True)
    NOA_Days = models.CharField(max_length=150, blank=True, null=True)
    NOA_Approved_By = models.CharField(max_length=150, blank=True, null=True)
    NOA_Approved_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    NOA_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    NOA_Attachment = models.FileField(upload_to='documents/NOA/', blank=True, null=True)

    PO_Date = models.CharField(max_length=150, blank=True, null=True)
    PO_Signatures = models.CharField(max_length=150, blank=True, null=True)
    PO_Pages = models.CharField(max_length=150, blank=True, null=True)
    PO_Days = models.CharField(max_length=150, blank=True, null=True)
    PO_Requested_By = models.CharField(max_length=150, blank=True, null=True)
    PO_Requested_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    PO_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    PO_Attachment = models.FileField(upload_to='documents/PO/', blank=True, null=True)
    
    PO_Approval_Date = models.CharField(max_length=150, blank=True, null=True)
    PO_Approval_Signatures = models.CharField(max_length=150, blank=True, null=True)
    PO_Approval_Pages = models.CharField(max_length=150, blank=True, null=True)
    PO_Approval_Days = models.CharField(max_length=150, blank=True, null=True)
    PO_Approved_By = models.CharField(max_length=150, blank=True, null=True)
    PO_Approved_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    PO2_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    PO_Approved_attachment = models.FileField(upload_to='documents/PO/', blank=True, null=True)

    Supplier_Name = models.CharField(max_length=150, blank=True, null=True)
    PO_Supplier_Date = models.CharField(max_length=150, blank=True, null=True)
    PO_Supplier_Signatures = models.CharField(max_length=150, blank=True, null=True)
    PO_Supplier_Pages = models.CharField(max_length=150, blank=True, null=True)
    PO_Supplier_Days = models.CharField(max_length=150, blank=True, null=True)
    Supplier_Modified_By = models.CharField(max_length=150, blank=True, null=True)
    Supplier_Modified_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    Supplier_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    PO_Supplier_attachment = models.FileField(upload_to='documents/PO/', blank=True, null=True)

    Delivery_Date = models.CharField(max_length=150, blank=True, null=True)
    Delivery_Signatures = models.CharField(max_length=150, blank=True, null=True)
    Delivery_Pages = models.CharField(max_length=150, blank=True, null=True)
    Delivery_Days = models.CharField(max_length=150, blank=True, null=True)
    Delivery_Inspected_By = models.CharField(max_length=150, blank=True, null=True)
    Delivery_Inspected_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    Delivery_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    Delivery_Attachment = models.FileField(upload_to='documents/Delivery/', blank=True, null=True)

    DV_Processing_Date = models.CharField(max_length=150, blank=True, null=True)
    DV_Signatures = models.CharField(max_length=150, blank=True, null=True)
    DV_Pages = models.CharField(max_length=150, blank=True, null=True)
    DV_Days = models.CharField(max_length=150, blank=True, null=True)
    DV_Modified_By = models.CharField(max_length=150, blank=True, null=True)
    DV_Modified_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    DV_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    DVProcessing_Attachment = models.FileField(upload_to='documents/DV/', blank=True, null=True)

    DV_Approval_Date = models.CharField(max_length=150, blank=True, null=True)
    DV_Approval_Signatures = models.CharField(max_length=150, blank=True, null=True)
    DV_Approval_Pages = models.CharField(max_length=150, blank=True, null=True)
    DV_Approval_Days = models.CharField(max_length=150, blank=True, null=True)
    DV_Approved_By = models.CharField(max_length=150, blank=True, null=True)
    DV_Approved_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    DV2_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    DVApproval_Attachment = models.FileField(upload_to='documents/DV/', blank=True, null=True)
    
    OR_CR_Request_Date = models.CharField(max_length=150, blank=True, null=True)
    OR_CR_Signatures = models.CharField(max_length=150, blank=True, null=True)
    OR_CR_Pages = models.CharField(max_length=150, blank=True, null=True)
    OR_CR_Days = models.CharField(max_length=150, blank=True, null=True)
    ORCR_Modified_By = models.CharField(max_length=150, blank=True, null=True)
    ORCR_Modified_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    ORCR_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    ORCR_Attachment = models.FileField(upload_to='documents/ORCR/', blank=True, null=True)

    Check_Releasing_Date = models.CharField(max_length=150, blank=True, null=True)
    Check_Signatures = models.CharField(max_length=150, blank=True, null=True)
    Check_Pages = models.CharField(max_length=150, blank=True, null=True)
    Check_Days = models.CharField(max_length=150, blank=True, null=True)
    Check_Recevied_By = models.CharField(max_length=150, blank=True, null=True)
    Check_Received_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    Check_Timestamp = models.DateField(auto_now=True, auto_now_add=False, blank=True, null=True)
    Checks_Attachment = models.FileField(upload_to='documents/Checks/', blank=True, null=True)
   
    Start_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    End_Date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    Total_LeadTime = models.CharField(max_length=150, blank=True, null=True)
    Total_Signatures = models.CharField(max_length=150, blank=True, null=True)
    Status = models.CharField(max_length=100, choices=choices, default="Completed")
    Document_Location = models.CharField(max_length=100, choices=locations, default="Procurement-Office")
    LastModified_Timestamp = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    Comments = models.TextField(max_length=5000, blank=True, default="--Comment Section--")
    Processed_By = models.CharField(max_length=150, blank=True, null=True)

    class Meta: 
            ordering = ('-Total_LeadTime',)
    def __str__(self):
        return self.Equipment

    def get_absolute_url(self):
        return reverse('accounts:procurement_edit', kwargs={'pk': self.pk})



