from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    email = models.EmailField()
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    job_list = models.TextField(blank=True, help_text="List of job responsibilities, one per line")
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.title} at {self.company}"
    
    def get_job_list(self):
        """Return job responsibilities as a list"""
        if self.job_list:
            return [job.strip() for job in self.job_list.split('\n') if job.strip()]
        return []

class Skill(models.Model):
    SKILL_TYPES = (
        ('technical', 'Technical'),
        ('software', 'Software'),
        ('language', 'Language'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=SKILL_TYPES, default='technical')
    
    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.DateField(default='2000-01-01')
    graduation_date = models.DateField()
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    thesis_name = models.CharField(max_length=255, blank=True, null=True)
    thesis_url = models.URLField(blank=True, null=True)
    
    class Meta:
        ordering = ['-graduation_date']
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    certificate_url = models.URLField(blank=True, null=True)
    
    class Meta:
        ordering = ['-issue_date']
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    technologies = models.CharField(max_length=500)
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    key_achievements = models.TextField(blank=True, help_text="List of key achievements, one per line")
    
    
    def __str__(self):
        return self.title
    
    def get_achievements_list(self):
        """Return achievements as a list"""
        if self.key_achievements:
            return [achievement.strip() for achievement in self.key_achievements.split('\n') if achievement.strip()]
        return []

class Recommendation(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    text = models.TextField()
    
    def __str__(self):
        return f"Recommendation from {self.name}"
