const puppeteer = require('puppeteer-core');

async function main() {
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/chromium',
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 800 });
  
  // 測試打開 Bing
  await page.goto('https://www.bing.com', { waitUntil: 'networkidle2' });
  
  const title = await page.title();
  console.log('標題:', title);
  
  // 截圖
  await page.screenshot({ path: '/tmp/bing_test.png' });
  console.log('截圖完成: /tmp/bing_test.png');
  
  await browser.close();
}

main().catch(console.error);
