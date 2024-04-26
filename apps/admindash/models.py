from django.utils import timezone
from django.utils.text import slugify
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="subcategory"
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )
    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Select Download Category"
    )
    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True
    )

    secondary_image = models.ImageField(
        upload_to="secondary_image/",
        blank=True,
        null=True
    )
    title = models.CharField(
        max_length=100
    )
    quoatation = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    files = models.FileField(
        upload_to="files/",
        null=True,
        blank=True
    )
    description = CKEditor5Field(
        'description',
        config_name='extends',
        blank=True,
        null=True
    )
    slug = models.SlugField(
        max_length=300,
        blank=True
    )
    link = models.URLField(
        max_length=100,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.pk:  # Object is being saved for the first time
            super().save(*args, **kwargs)  # Call save method to generate pk
        if not self.slug:
            title_without_span = self.title.replace("span", "")
            self.slug = slugify(f"{title_without_span}-{self.pk}")
            super().save(*args, **kwargs)  # Call save again to update slug
        else:
            super().save(*args, **kwargs)  # If slug already exists, save as usual

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=225, blank=True, null=True)
    subject = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    message = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class ApplyAsStudent(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField(blank=True, null=True)
    faculty = models.CharField(max_length=100, blank=True, null=True)
    pass_out_year = models.CharField(max_length=4, blank=True, null=True)
    percentage = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    apply_for_country = models.CharField(
        max_length=100, blank=True, null=True)
    english_proficiency_test = models.CharField(
        max_length=100, blank=True, null=True)
    score = models.CharField(max_length=10, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class ApplyAsAgent(models.Model):
    full_name = models.CharField(max_length=255)
    education = models.CharField(max_length=100, blank=True, null=True)
    consultancy_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    years_of_experience = models.CharField(
        max_length=50, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False, blank=True, null=True)
    created_date = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.full_name
