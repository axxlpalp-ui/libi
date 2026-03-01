const puppeteer = require('puppeteer-core');

async function main() {
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/chromium',
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 800 });
  
  // 打開 Gmail 註冊頁面
  console.log('打開 Gmail 註冊頁面...');
  await page.goto('https://accounts.google.com/signup', { waitUntil: 'networkidle2' });
  
  // 截圖
  await page.screenshot({ path: '/tmp/gmail_signup.png' });
  console.log('截圖完成');
  
  // 取得標題
  const title = await page.title();
  console.log('標題:', title);
  
  await browser.close();
}

main().catch(console.error);
