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


class Title(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
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

    def save(self, *args, **kwargs):
        if not self.slug:
            title_without_span = self.title.replace(
                "span", "")  # Removing "span" from the title
            self.slug = slugify(f"{title_without_span}")
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=225, blank=True, null=True)
    subject = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    message = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class ApplyAsStudent(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    faculty = models.CharField(max_length=100)
    pass_out_year = models.CharField(max_length=4)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    apply_for_country = models.CharField(max_length=100)
    english_proficiency_test = models.CharField(max_length=100)
    score = models.CharField(max_length=10)
    remarks = models.TextField()
    is_read = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class ApplyAsAgent(models.Model):
    full_name = models.CharField(max_length=255)
    education = models.CharField(max_length=100)
    consultancy_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    years_of_experience = models.CharField(max_length=50)
    remarks = models.TextField()
    is_read = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
