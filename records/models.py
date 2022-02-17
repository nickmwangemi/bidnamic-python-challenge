from django.db import models

"""
adgroups
- ad_group_id
- campaign_id
- alias
- status
"""


class AdGroup(models.Model):
    ad_group_id = models.BigIntegerField()
    campaign_id = models.BigIntegerField()
    alias = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"AdGroup object with {self.ad_group_id} has been created."


"""
campaigns
- campaign_id
- structure_value
- status
"""


class Campaign(models.Model):
    campaign_id = models.BigIntegerField()
    structure_value = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Campaign object with {self.campaign_id} has been created."


"""
search_terms
- date
- ad_group_id
- campaign_id
- clicks
- cost
- conversion_value
- conversions
- search_term
"""


class SearchTerm(models.Model):
    date = models.DateField()
    ad_group_id = models.BigIntegerField()
    campaign_id = models.BigIntegerField()
    clicks = models.BigIntegerField()
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    conversion_value = models.DecimalField(max_digits=5, decimal_places=2)
    conversions = models.BigIntegerField()
    search_term = models.CharField(max_length=255)

    def __str__(self):
        return f"SearchTerm object with {self.campaign_id} has been created."
