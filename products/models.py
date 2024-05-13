from django.db.models import Model, CharField, DateTimeField, ForeignKey, CASCADE, TextField, IntegerField, \
    BooleanField, SlugField, ImageField
from django.utils.text import slugify
from unidecode import unidecode


class Product(Model):
    slug = SlugField(max_length=100, unique=True)
    name = CharField(max_length=100)
    description = TextField()
    price = IntegerField()
    is_sale = BooleanField(default=False)
    is_active = BooleanField(default=False)
    is_available = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Check if slug is not already set
            latin_title = unidecode(self.name)
            self.slug = slugify(latin_title)  # Generate slug based on Latin title

            original_slug = self.slug
            counter = 1
            while Product.objects.filter(slug=self.slug).exists():
                self.slug = '{}-{}'.format(original_slug, counter)
                counter += 1

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']
        unique_together = (('name', 'slug'),)
        index_together = (('name', 'slug'),)

    def __str__(self):
        return self.name


class Image(Model):
    image = ImageField(upload_to='images/products/')
    product = ForeignKey("products.Product", on_delete=CASCADE)
