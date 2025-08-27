import helpers
from django.core.management.base import BaseCommand
from typing import Any
from django.conf import settings

class Command(BaseCommand):
    help = "Downloads vendor static files"

    STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')
    #the name represents the path in the folder of downloading carefully assing to match the static files
    VENDOR_STATIC_FILES = {
        # URLs for vendor static files
        # 'url1': 'https://www.example.com/static/file.js',
        # 'url2': 'https://www.example.com/static/file.css',
    }

    def handle(self, *args: Any, **options: Any):
        self.stdout.write("CbeSync --Downloading cdn static files")

        completed_urls = []
        for name, url in self.VENDOR_STATIC_FILES.items():
            out_path = self.STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
                print(f"{name}: {url}- {out_path}")
            else:
                self.stdout.write(self.style.ERROR(f"failed to download {url}"))

        if set(completed_urls) == set(self.VENDOR_STATIC_FILES.values()):
            self.stdout.write(self.style.SUCCESS("downloaded all static files successfully"))
        else:
            self.stdout.write(self.style.WARNING("Somefiles were not dowloaded"))