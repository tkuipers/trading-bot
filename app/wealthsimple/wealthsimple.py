import random
import time
from typing import Optional
import pyotp

from playwright.async_api import async_playwright, BrowserContext, Browser, Page
from app.trading_platform import TradingPlatform


class WealthSimple(TradingPlatform):
    def __init__(self, username: str, password: str, secret: str):
        self.username = username
        self.password = password
        self.otp_secret = secret
        self.initialized = False
        self.playwright = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None

    async def initialize(self):
        if not self.initialized:
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=False)
            self.context = await self.browser.new_context()
            self.page = await self.context.new_page()
            await self.page.goto("https://my.wealthsimple.com/app/login")
            await self.page.wait_for_load_state('networkidle')
            self.initialized = True

    async def close(self):
        if self.page:
            await self.page.close()
        if self.context:
            await self.context.close()
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    def __del__(self):
        self.close()

    async def __fill(self, selector: str, text:str):
        await self.page.wait_for_selector(selector)
        element = await self.page.query_selector(selector)
        if element:
            await element.click()
            await self.__type(text)

    async def __wait(self):
        time.sleep(random.uniform(0.05, 0.15))

    async def __type(self, text: str):
        for char in text:
            await self.__wait()
            await self.page.keyboard.press(char)

    async def login(self):
        await self.initialize()
        input_selector = f"*[inputmode='email']"
        await self.__fill(input_selector, self.username)
        input_selector = f"*[type='password']"
        await self.__fill(input_selector, self.password)
        await self.__wait()
        await self.page.keyboard.press("Enter")
        await self.page.wait_for_load_state('networkidle')
        input_selector = f"*[autocomplete='one-time-code']"
        totp = pyotp.TOTP(self.otp_secret)
        await self.__fill(input_selector, totp.now())
        await self.__wait()
        await self.page.keyboard.press("Enter")
        await self.page.wait_for_load_state('networkidle')
        await self.page.wait_for_selector(f"*[inputmode='search']")
        print(await self.page.title())

    async def get_portfolio(self):
        # Get the user's portfolio
        pass

    async def get_account(self):
        # Get the user's account
        pass

    async def get_transactions(self):
        # Get the user's transactions
        pass

    async def buy(self, symbol, quantity):
        # Buy a stock
        pass

    async def sell(self, symbol, quantity):
        # Sell a stock
        pass
