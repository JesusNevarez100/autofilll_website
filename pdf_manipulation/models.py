from django.db import models
# from smartfields import fields


# Create your models here.


class UploadedPDF(models.Model):
    DEAL_CHOICES     = (
        ('cash', 'Cash Deal'),
        ('finance', 'Finance Deal'),
        ('both', 'Both'),
    )
    
    pdf_file = models.FileField(upload_to='uploaded_pdfs/')
    deal_type = models.CharField(max_length=10, choices=DEAL_CHOICES)
    # linked_client_info = fields.LazyForeignKey('clients.Client', on_delete=models.SET_NULL, null=True, blank=True)
    # linked_vehicle_info = fields.LazyForeignKey('vehicles.Vehicle', on_delete=models.SET_NULL, null=True, blank=True)
    text_boxes = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.pdf_file.name



