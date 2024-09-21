import puppeteer from "puppeteer";

/**
 * This script is used to take screenshots of deer abundance charts provided by the WI DNR
 */

const browser = await puppeteer.launch({ headless: true });
const page = await browser.newPage();
const outputDir = "pop_images";

await page.goto("https://apps.dnr.wi.gov/deermetrics/DeerStats.aspx?R=2");
const options = await page.evaluate(() =>
  Array.from(document.querySelectorAll("#cphBody_ddlCounty option")).map(
    (el) => ({ val: el.value, name: el.innerHTML })
  )
);
const start = 1;
const end = options.length;

for (var i = start; i < end; i++) {
  await page.select("#cphBody_ddlCounty", options[i].val);
  await page.waitForNetworkIdle();
  const chartEl = await page.waitForSelector("#cphBody_tdRight");
  await chartEl.screenshot({ path: `${outputDir}/${options[i].name}.png` });
}
await browser.close();
