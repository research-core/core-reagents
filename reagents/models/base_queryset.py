from django.db import models
from django.db.models import Q
from django.utils import timezone

class ReagentsBaseQuerySet(models.QuerySet):


    def list_permissions(self, user):
        """
        Everyone has access to all antibodies
        """
        return self

    def has_view_permissions(self, user):
        """
        Everyone can see all the publications.
        """
        return True

    def has_add_permissions(self, user):
        """
        All users are allowed to add new publications.
        """
        return True

    def has_update_permissions(self, user):
        """
        Returns the queryset of objects the user can change.
        """
        if user.is_superuser:
            return True

        now = timezone.now()
        return self.filter(
            Q(lab__group__isnull=True) |
            Q(
                lab__group__groupmember__date_joined__lte=now,
                lab__group__groupmember__date_left__gte=now,
                lab__group__groupmember__person__djangouser=user
            ) |
            Q(
                lab__group__groupmember__date_joined__lte=now,
                lab__group__groupmember__date_left__isnull=True,
                lab__group__groupmember__person__djangouser=user
            ) |
            Q(
                lab__group__groupmember__date_joined__isnull=True,
                lab__group__groupmember__date_left__isnull=True,
                lab__group__groupmember__person__djangouser=user
            )
        ).exists()


    def has_remove_permissions(self, user):
        """
        Returns the queryset of objects the user can delete.
        """
        if user.is_superuser:
            return True

        now = timezone.now()
        return self.filter(
            Q(lab__group__isnull=True) |
            Q(
                lab__group__groupmember__date_joined__lte=now,
                lab__group__groupmember__date_left__gte=now,
                lab__group__groupmember__person__djangouser=user
            ) |
            Q(
                lab__group__groupmember__date_joined__lte=now,
                lab__group__groupmember__date_left__isnull=True,
                lab__group__groupmember__person__djangouser=user
            ) |
            Q(
                lab__group__groupmember__date_joined__isnull=True,
                lab__group__groupmember__date_left__isnull=True,
                lab__group__groupmember__person__djangouser=user
            )
        ).exists()