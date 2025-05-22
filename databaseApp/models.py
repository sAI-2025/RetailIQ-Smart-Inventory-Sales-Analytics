from django.db import models
from django.utils import timezone
from datetime import datetime


class OrderDetails(models.Model):
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)
    
    order_id = models.CharField(max_length=50)
    payment_id = models.CharField(max_length=50)
    device_id = models.IntegerField()
    
    ordered_vanilla = models.IntegerField(default=0)
    ordered_chocolate = models.IntegerField(default=0)
    ordered_strawberry = models.IntegerField(default=0)
    
    delivered_vanilla = models.IntegerField(default=0)
    delivered_chocolate = models.IntegerField(default=0)
    delivered_strawberry = models.IntegerField(default=0)
    
    is_payment_successful = models.BooleanField(default=False)
    our_order_id = models.BigIntegerField()
    is_all_items_delivered = models.BooleanField(default=False)
    
    # Soft delete fields
    deleted_at = models.DateTimeField(null=True, blank=True)  # Timestamp for soft deletes
    
    def soft_delete(self):
        """Marks the order as deleted by setting deleted_at to the current time."""
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """Restores a soft-deleted order."""
        self.deleted_at = None
        self.save()

    @property
    def is_deleted(self):
        """Returns whether the order is soft-deleted."""
        return self.deleted_at is not None
    
    def __str__(self):
        return f"{self.date}---{self.time}---{self.order_id} ---- {self.device_id} --- {self.is_payment_successful}"


class ProductStock(models.Model):
    product_id = models.IntegerField(unique=True)
    vanilla = models.IntegerField(default=0)
    chocolate = models.IntegerField(default=0)
    strawberry = models.IntegerField(default=0)

    def __str__(self):
        return f"Product {self.product_id}"

    class Meta:
        verbose_name = 'Product Stock'
        verbose_name_plural = 'Product Stocks'
