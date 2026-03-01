const puppeteer = require('puppeteer-core');

async function main() {
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/chromium',
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  const page = await browser.newPage();
  await page.goto('https://www.jx3box.com/bps/104328', { waitUntil: 'networkidle2' });
  
  const content = await page.evaluate(() => {
    return document.body.innerText;
  });
  
  console.log(content.substring(0, 10000));
  await browser.close();
}

main().catch(console.error);
