# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.fields import PlaceholderField

from shop.money.fields import MoneyField
from .product import Product
from django.contrib.auth.models import Profile

from django.utils import timezone


class Membership(Product):
    """
    This Commodity model inherits from polymorphic Product, and therefore has to be redefined.
    """
    unit_price = MoneyField(
        _("Unit price"),
        decimal_places=3,
        help_text=_("Net price for this product"),
    )

    product_code = models.CharField(
        _("Product code"),
        max_length=255,
        unique=True,
    )
    
    signup_date = models.DateField(
        _("Signed Up"),
        default = timezone.now,
    )
    
    profile = models.ForeignKey(Profile, null=True, blank=True)

    # controlling the catalog
    placeholder = PlaceholderField("Membership Details")
    show_breadcrumb = True  # hard coded to always show the product's breadcrumb

    class Meta:
        verbose_name = _("Membership")

    def get_price(self, request):
        return self.unit_price