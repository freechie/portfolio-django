import magic
from django.core.exceptions import ValidationError

def validate_file_size(value):
    max_size = 10 * 1024 * 1024  # 10MB limit
    if value.size > max_size:
        raise ValidationError('The maximum file size that can be uploaded is 10MB')
    return value

def validate_file_type(value):
    # Read the first 2048 bytes to determine the file type
    file_content = value.read(2048)
    value.seek(0) # Reset file pointer
    
    mime_type = magic.from_buffer(file_content, mime=True)
    
    valid_mime_types = [
        'image/jpeg', 
        'image/png', 
        'image/webp', 
        'application/pdf'
    ]
    
    if mime_type not in valid_mime_types:
        raise ValidationError(f'Unsupported file type: {mime_type}. Only JPEG, PNG, WEBP and PDF are allowed.')
    return value