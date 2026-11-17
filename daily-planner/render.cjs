// Renders planner.html to an A4 PDF and a 300-DPI PNG preview.
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const dir = __dirname;
  const url = 'file://' + path.join(dir, 'planner.html');
  const browser = await chromium.launch();

  // PDF (vector, A4 portrait)
  const page = await browser.newPage();
  await page.goto(url);
  await page.evaluate(() => document.fonts.ready);
  const over = await page.evaluate(() => {
    const p = document.querySelector('.page');
    return p.scrollHeight - p.clientHeight;
  });
  if (over > 0) console.warn('WARNING: content overflows page by', over, 'px');
  await page.pdf({ path: path.join(dir, 'daily-planner.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });

  // PNG at 300 DPI: 210mm = 793.7 CSS px; 2480 px / 793.7 = 3.1246
  const png = await browser.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2480 / 793.7 });
  await png.goto(url);
  await png.evaluate(() => document.fonts.ready);
  await png.screenshot({ path: path.join(dir, 'daily-planner-300dpi.png'), clip: { x: 0, y: 0, width: 793.7, height: 1122.5 } });

  await browser.close();
  console.log('done');
})();
