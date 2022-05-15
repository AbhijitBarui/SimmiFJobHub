from django.db import models

class Jobs(models.Model):
    role = models.CharField(max_length=50)
    experience = models.CharField(max_length=10)
    opening_count = models.IntegerField(default=1)
    location = models.TextField()
    expected_salary = models.DecimalField(decimal_places=2,max_digits=10)
    keyskills = models.TextField()
    job_description = models.TextField()
    employment_type = models.CharField(max_length=20)
    education = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.role
    

class Application(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    location = models.TextField()
    resume = models.FileField()
    reviewed = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.job.role