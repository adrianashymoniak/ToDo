import hashlib

from django.utils import timezone


def get_first_name(obj):
    chunks = obj.name.split()
    if len(chunks) >= 1:
        return chunks[0]
    return ""


def get_last_name(obj):
    chunks = obj.name.split()
    if len(chunks) >= 2:
        return chunks[1]
    return ""


def days_on_site(obj):
    delta = timezone.now() - obj.date_joined
    return delta.days


def get_email_md5_hash(obj):
    return hashlib.md5(obj.email.lower().encode("utf-8")).hexdigest()
