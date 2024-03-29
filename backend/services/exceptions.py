from rest_framework.exceptions import PermissionDenied, ValidationError


class BadRequestException(ValidationError):
    """Исключение для некорректных данных."""

    default_detail = "модель с таким названием уже существует"


class AlreadyExistsException(PermissionDenied):
    pass
