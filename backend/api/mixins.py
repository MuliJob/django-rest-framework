"""Permission Mixins"""
from rest_framework import permissions

from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    """Permission Mixins"""
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
