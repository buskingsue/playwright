import asyncio  # 비동기 처리를 위한 asyncio
from playwright.async_api import async_playwright  # 비동기 Playwright 사용

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # GitHub Actions는 headless=True 필수
        context = await browser.new_context(viewport=None)
        page = await context.new_page()
        await page.goto("https://www.naver.com")
        await asyncio.sleep(5)
        await page.screenshot(path="naver.png", full_page=True)
        await browser.close()

asyncio.run(main())
