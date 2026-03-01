const puppeteer = require('puppeteer-core');

async function main() {
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/chromium',
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 800 });
  
  // 打開 Gmail 主頁面
  console.log('打開 Gmail...');
  await page.goto('https://mail.google.com/mail/u/0/#inbox', { waitUntil: 'networkidle2', timeout: 30000 });
  
  // 截圖
  await page.screenshot({ path: '/tmp/gmail_explore.png' });
  console.log('截圖完成');
  
  const title = await page.title();
  console.log('標題:', title);
  
  await browser.close();
}

main().catch(console.error);
