from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    class Role(models.IntegerChoices):
        STUDENT = 1, "Student"
        TUTOR = 2, "Tutor"
        FREELANCER = 3, "Freelancer"
        MENTOR = 4, "Mentor"

    role_level = models.PositiveSmallIntegerField(
        choices=Role.choices, default=Role.STUDENT
    )
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def role(self) -> str:
        return self.get_role_level_display()

    @property
    def can_browse(self) -> bool:
        return True

    @property
    def can_post_tutor(self) -> bool:
        return self.role_level >= self.Role.TUTOR

    @property
    def can_take_jobs(self) -> bool:
        return self.role_level >= self.Role.FREELANCER

    @property
    def can_post_mentor(self) -> bool:
        return self.role_level >= self.Role.MENTOR
