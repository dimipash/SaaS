import helpers
from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand

STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js",
    "flowbite.min.js.map": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js",
}

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write("Downloading vendor static files")
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            output_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, output_path)
            if dl_success:
                completed_urls.append(url)
                self.stdout.write(f"Downloaded {name}")
            else:
                self.stdout.write(f"Failed to download {name}")
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write("All vendor static files downloaded")     
        else:
            self.stdout.write("Failed to download all vendor static files")