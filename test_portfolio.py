import pytest
from playwright.sync_api import Page, expect

def test_homepage_loads_correctly(page: Page):
    page.goto("https://deepthi-s-hub.web.app/")
    expect(page).to_have_title("Bug & Logic By DM")
    page.screenshot(path="portfolio_homepage.png")


def test_linkedin_hyperlink_works(page: Page):
   
    page.goto("https://deepthi-s-hub.web.app/")     
    linkedin_link = page.locator("a[href*='linkedin.com']")  
    expect(linkedin_link).to_be_visible()
       

    target_url = linkedin_link.get_attribute("href")
    print(f"\n[INFO] Found LinkedIn URL: {target_url}")
    assert target_url is not None and "linkedin.com/in/" in target_url
      
    with page.expect_popup() as popup_info:
        linkedin_link.click()
    
    new_tab = popup_info.value
    new_tab.wait_for_load_state("domcontentloaded")
    
    
    assert "linkedin.com" in new_tab.url
    print(f"[SUCCESS] Successfully verified navigation to: {new_tab.url}")

