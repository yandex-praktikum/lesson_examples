"""Настройка существующего requests-html для Python 3.14 и локального Chrome."""
import asyncio
import os
import shutil
from pathlib import Path

import pyppeteer
from requests_html import HTMLSession


def find_browser():
    configured = os.environ.get('PARSING_BROWSER_PATH')
    if configured:
        if not Path(configured).is_file():
            raise FileNotFoundError('Проверьте PARSING_BROWSER_PATH: ' + configured)
        return configured
    candidates = [
        shutil.which('google-chrome'), shutil.which('chromium'),
        shutil.which('chromium-browser'),
        str(Path(os.environ.get('PROGRAMFILES', 'C:/Program Files')) / 'Google/Chrome/Application/chrome.exe'),
        str(Path(os.environ.get('PROGRAMFILES(X86)', 'C:/Program Files (x86)')) / 'Google/Chrome/Application/chrome.exe'),
        str(Path(os.environ.get('LOCALAPPDATA', 'C:/Users/Default/AppData/Local')) / 'Google/Chrome/Application/chrome.exe'),
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '/Applications/Chromium.app/Contents/MacOS/Chromium',
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    raise FileNotFoundError('Установите Chrome/Chromium или задайте PARSING_BROWSER_PATH.')


class BrowserHTMLSession(HTMLSession):
    """Синхронная сессия requests-html с явным циклом и путём браузера."""

    def __init__(self):
        super().__init__(browser_args=[])
        self.browser_path = find_browser()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    @property
    def browser(self):
        if not hasattr(self, '_browser'):
            self._browser = self.loop.run_until_complete(pyppeteer.launch(
                executablePath=self.browser_path, headless=True,
            ))
        return self._browser

    def close(self):
        if self.loop.is_closed():
            return
        try:
            super().close()
        finally:
            self.loop.close()
            asyncio.set_event_loop(None)
