from django.db import models

JOB_ROLES = [
    ("SDE", "Software Development Engineer (7 LPA)"),
    ("DA", "Data Analyst (7 LPA)"),
    ("WD", "Web Developer (7 LPA)"),
    ("QA", "Quality Assurance Engineer (7 LPA)"),
    ("DS", "Data Scientist (7 LPA)"),
    ("DBA", "Database Administrator (7 LPA)"),

    ("HR", "HR Executive (4 LPA)"),
    ("SE", "Support Engineer (4 LPA)"),
    ("IT", "IT Administrator (4 LPA)"),
    ("BA", "Business Analyst (4 LPA)"),
    ("TS", "Technical Support (4 LPA)"),
]

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    age = models.IntegerField()
    job_role = models.CharField(max_length=50, choices=JOB_ROLES)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return self.name
