from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill,Transpose
from taggit.managers import TaggableManager


WING = [
    ('ARMY', 'ARMY'),
    ('NAVY', 'NAVY'),
    ('AIR FORCE', 'AIR FORCE'),
    ('TECHNOLOGY', 'TECHNOLOGY'),
    ('ANONYMOUS Media', 'ANONYMOUS Media'),
    ('DIGITAL ART', 'DIGITAL ART'),
    ('CONTENT CREATION', 'CONTENT CREATION'),
    ('SOCIAL ACTIVISM', 'SOCIAL ACTIVISM'),
    ('MENTAL WELLNESS', 'MENTAL WELLNESS'),
    ('HOBBIES & INTERESTS', 'HOBBIES & INTERESTS')
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, blank=True)
    image = models.ImageField(upload_to='profile_pics')
    image_thumbnail_user = ImageSpecField(
        source='image',
        processors=[Transpose(), ResizeToFill(170, 170)],
        format='JPEG',
        options={'quality': 100}
    )
    description = models.CharField(max_length=100, blank=True)
    follows = models.ManyToManyField(User, related_name="follows", blank=True)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    camps = TaggableManager(blank=True)
    wing = models.CharField(max_length=50, choices=WING, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"



REASON = [
    ('SPAM', 'SPAM'),
    ('INAPPROPRIATE', 'INAPPROPRIATE'),
    ('HARASSMENT', 'HARASSMENT'),
    ('HATE SPEECH', 'HATE SPEECH'),
    ('FAKE NEWS', 'FAKE NEWS'),
    ('IMPERSONATION', 'IMPERSONATION'),
    ('OBSCENE CONTENT', 'OBSCENE CONTENT'),
    ('SEXUAL CONTENT', 'SEXUAL CONTENT'),
    ('VIOLENCE', 'VIOLENCE'),
    ('PLAGIARISM', 'PLAGIARISM'),
    ('SCAM', 'SCAM'),
    ('UNSAFE LINKS', 'UNSAFE LINKS'),
    ('MALICIOUS CONTENT', 'MALICIOUS CONTENT'),
    ('THREATENING BEHAVIOR', 'THREATENING BEHAVIOR'),
    ('MATURE CONTENT', 'MATURE CONTENT'),
    ('SELF-HARM', 'SELF-HARM')
]

class UserReport(models.Model):
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reported_user')
    reason = models.CharField(max_length=50,choices=REASON)
    reporting_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reporting_user')
    date_reported = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reported_user.username