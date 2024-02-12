import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://example.com')  # Replace 'https://example.com' with your target website URL

        # Find all input elements
        inputs = await page.query_selector_all('input')
        
        if inputs:
            # Choose a random input element
            input_element = random.choice(inputs)
            
            # Type "hello" into the selected input
            await input_element.type('hello')
        
        # Find all button elements
        buttons = await page.query_selector_all('button')
        
        if buttons:
            # Choose a random button element
            button_element = random.choice(buttons)
            
            # Click the selected button
            await button_element.click()

        await browser.close()

asyncio.run(main())
