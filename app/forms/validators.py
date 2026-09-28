import re
from urllib.parse import urlparse
from wtforms.validators import ValidationError


def https_url(form, field):
    """Only allow absolute http(s) image URLs (blocks javascript:, data:, etc.)."""
    value = (field.data or '').strip()
    if not value:
        return
    parsed = urlparse(value)
    if parsed.scheme not in ('http', 'https') or not parsed.netloc:
        raise ValidationError('Must be a valid http(s) URL.')
    field.data = value


def digits_between(min_len, max_len, message):
    def _check(form, field):
        digits = re.sub(r'\D', '', field.data or '')
        if not (min_len <= len(digits) <= max_len):
            raise ValidationError(message)
    return _check


def strip(value):
    return value.strip() if isinstance(value, str) else value
