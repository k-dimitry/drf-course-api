from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from api.models import Product


@receiver(signal=[post_save, post_delete], sender=Product)
def invalidate_product_cache(sender, instance, **kwargs):
    """
    Invalidates product list caches when a product is created, updated or deleted.
    """
    print('Clearing product cache')
    cache.delete_pattern('*product_list*')
