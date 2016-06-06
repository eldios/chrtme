class Chrtme:
    """Base chrtme library class"""

    @classmethod
    def _validate_url(cls, url):
        """Validate URLs used to download images"""
        from urllib.parse import urlparse
        parsed_url = urlparse(url)
        allowed_schemes = [
            'http', 'https',
            'file'
        ]
        if not (
            parsed_url.scheme or
            parsed_url.scheme in allowed_schemes
        ):
            raise ValueError("Invalid URL scheme: http, https and file only.")
        return parsed_url.geturl()

    @classmethod
    def _validate_location(cls, location):
        """Validate target chrootfs location"""
        import os
        if not (
            os.path.exists(location) or
            os.path.exists( # location parent directory
                os.path.abspath(
                    os.path.join(location, os.path.pardir)
                )
            )
        ):
            raise ValueError("Specified location and parent directory don't exist")

    def __init__(self, url, cmd, location=None):
        # URL
        try:
            self._url = self._validate_url(url)
        except:
            raise

        # CMD
        self._cmd = cmd

        # Location
        if not location:
            import os
            location = os.path.join(os.getcwd(), 'chrootfs')

        try:
            self._location = self._validate_location(location)
        except:
            raise
