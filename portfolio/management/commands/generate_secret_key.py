from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key
import os
import re


class Command(BaseCommand):
    help = 'Generate a new SECRET_KEY and update .env file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--env-file',
            type=str,
            default='.env',
            help='Path to .env file (default: .env)',
        )

    def handle(self, *args, **options):
        env_file = options['env_file']
        
        # Generate new secret key using Django's built-in function
        new_secret_key = get_random_secret_key()
        
        try:
            # Read current .env file
            if os.path.exists(env_file):
                with open(env_file, 'r') as file:
                    content = file.read()
                
                # Pattern to match SECRET_KEY line
                secret_key_pattern = r'^SECRET_KEY=.*$'
                
                # Check if SECRET_KEY exists
                if re.search(secret_key_pattern, content, re.MULTILINE):
                    # Replace existing SECRET_KEY
                    new_content = re.sub(
                        secret_key_pattern, 
                        f'SECRET_KEY={new_secret_key}', 
                        content, 
                        flags=re.MULTILINE
                    )
                    self.stdout.write(
                        self.style.SUCCESS(f'✅ SECRET_KEY updated in {env_file}')
                    )
                else:
                    # Add SECRET_KEY at the beginning if it doesn't exist
                    new_content = f'SECRET_KEY={new_secret_key}\n{content}'
                    self.stdout.write(
                        self.style.SUCCESS(f'✅ SECRET_KEY added to {env_file}')
                    )
                
                # Write back to file
                with open(env_file, 'w') as file:
                    file.write(new_content)
                
            else:
                # Create new .env file if it doesn't exist
                with open(env_file, 'w') as file:
                    file.write(f'SECRET_KEY={new_secret_key}\n')
                
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Created {env_file} with new SECRET_KEY')
                )
            
            self.stdout.write(
                self.style.WARNING(f'🔑 New SECRET_KEY: {new_secret_key}')
            )
            self.stdout.write(
                self.style.WARNING('⚠️  Remember to restart your application/container!')
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error updating SECRET_KEY: {str(e)}')
            )