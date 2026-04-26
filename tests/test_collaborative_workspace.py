import pytest
from playwright.sync_api import Page, expect
import os
import re

def test_collaborative_workspace_loads(page: Page):
    # Construct the absolute path to the HTML file
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = f"file://{current_dir}/collaborative_workspace/code.html"

    # Set viewport to desktop
    page.set_viewport_size({"width": 1280, "height": 800})

    # Load the page
    page.goto(file_path)

    # Verify the title contains "Collaborative Workspace" to accommodate variations
    expect(page).to_have_title(re.compile(r"Collaborative Workspace", re.IGNORECASE))

    # Verify Active Team Section
    expect(page.locator("h2", has_text="Active Team Nodes")).to_be_visible()
    expect(page.locator("text=Dr. Sarah Jenkins")).to_be_visible()
    expect(page.locator("text=Marcus Vance")).to_be_visible()

    # Verify Shared Vectors Section
    expect(page.locator("h2", has_text="Shared Vectors")).to_be_visible()
    expect(page.locator("text=Project Cerberus")).to_be_visible()
    expect(page.locator("h3", has_text="Shell Corp Matrix")).to_be_visible()

    # Verify Neural Feed Section
    expect(page.locator("h2", has_text="Neural Feed")).to_be_visible()

    # Ensure there are feed items
    feed_items = page.locator("p.leading-relaxed")
    expect(feed_items.first).to_be_visible()

def test_mobile_navigation(page: Page):
    # Construct the absolute path to the HTML file
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = f"file://{current_dir}/collaborative_workspace/code.html"

    # Set viewport to mobile to check bottom nav
    page.set_viewport_size({"width": 375, "height": 812})
    page.goto(file_path)

    expect(page.locator("nav.fixed.bottom-0")).to_be_visible()
