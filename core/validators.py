import os
from django.core.exceptions import ValidationError

CONTENT_TYPES = ['.pdf']
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = "10485760"


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    if not ext.lower() in CONTENT_TYPES:
        raise ValidationError(u'Unsupported file extension. Allow only PDF file')
    elif value.size > 10485760:
        raise ValidationError('File above 10MB. Please, send a file below 10 MiB.')
