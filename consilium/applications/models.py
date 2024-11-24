from django.db import models


class GrantApplication(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    title_of_request = models.CharField(max_length=255)
    funding_summary = models.TextField()
    how_spend_grant = models.TextField()
    importance_of_grant = models.TextField()
    goals = models.TextField()
    required_date = models.DateField()
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    funding_in_place = models.TextField(blank=True, null=True)
    benefit_description = models.TextField()
    commitment_description = models.TextField()
    barriers_description = models.TextField(blank=True, null=True)
    result_availability = models.TextField(blank=True, null=True)
    heard_from = models.CharField(max_length=255, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    previous_application_details = models.TextField(blank=True, null=True)
    evaluation_proposal = models.TextField(blank=True, null=True)
    support_network = models.TextField(blank=True, null=True)
    other_support = models.TextField(blank=True, null=True)
    applicant_signature = models.CharField(max_length=255)
    signed_date = models.DateField()
    parent_signature = models.CharField(max_length=255, blank=True, null=True)
    parent_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + " - " + self.title_of_request
