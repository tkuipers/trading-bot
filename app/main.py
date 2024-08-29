from fastapi import FastAPI
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

app = FastAPI()


@app.get("/")
async def root():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        # Open a new page
        page = await context.new_page()
        await stealth_async(page)
        await page.goto("https://my.wealthsimple.com/app/login")
        title = await page.title()
        print(f'The page title is: {title}')

    return {"message": "Hello World"}