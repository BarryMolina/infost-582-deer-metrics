import puppeteer from "puppeteer";

/**
 * This script is used to systematically download PDF deer reports for every county in WI
 */

const browser = await puppeteer.launch({ headless: true });
const page = await browser.newPage();

await page.goto("https://apps.dnr.wi.gov/deermetrics/PrintReport.aspx");
const options = await page.evaluate(() =>
  Array.from(document.querySelectorAll("#cphBody_ddlCounty option")).map(
    (el) => el.value
  )
);
const start = 1;
const end = options.length;

for (var i = start; i < end; i++) {
  await page.select("#cphBody_ddlCounty", options[i]);
  await page.click("#cphBody_btnNext");
}
await browser.close();
