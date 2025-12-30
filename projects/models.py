from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.FileField(upload_to="project_images/", blank=True)
    github_url = models.URLField(max_length=200, blank=True, null=True)
    code_snippet = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title