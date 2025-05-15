import requests
from bs4 import BeautifulSoup
import os
import re
import time
import random

def get_all_post_urls(blog_list_url):
    """블로그 목록 페이지에서 모든 게시물의 URL을 추출"""
    all_post_urls = []
    page_num = 1
    max_pages = 50 
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    blog_id = re.search(r'blogId=([^&]+)', blog_list_url).group(1)
    base_url = f"https://m.blog.naver.com/PostList.naver?blogId={blog_id}"
    
    while page_num <= max_pages:
        current_page_url = f"https://blog.naver.com/PostList.naver?from=postList&blogId=mukjjippa_boardgame&categoryNo=6&currentPage={page_num}"
        print(f"게시물 목록 페이지 {page_num} 스캔 중...")
        
        try:
            response = requests.get(current_page_url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            post_links = soup.select('.list_item a.link_title, .list_item a.link_post, .postlist a')
            
            if not post_links: 
                post_links = soup.select('div.list_item > a, .tab_detail a, .detail_post a')
            
            if not post_links: 
                post_links = soup.select('a[href*="PostView.naver"]')
            
            new_urls_count = 0
            
            for link in post_links:
                href = link.get('href')
                if href and 'PostView.naver' in href:
                    if not href.startswith('http'):
                        if href.startswith('/'):
                            href = f"https://m.blog.naver.com{href}"
                        else:
                            href = f"https://m.blog.naver.com/{href}"
                    
                    if href not in all_post_urls:
                        all_post_urls.append(href)
                        new_urls_count += 1
            
            print(f"페이지 {page_num}에서 {new_urls_count}개의 새 게시물 URL을 찾았습니다.")
            
            page_num += 1
            
            if new_urls_count == 0:
                print("더 이상 새 게시물이 없습니다. 스캔을 종료합니다.")
                break
                
            time.sleep(random.uniform(1.0, 3.0))
            
        except Exception as e:
            print(f"페이지 {page_num} 스캔 중 오류 발생: {e}")
            break
    
    print(f"총 {len(all_post_urls)}개의 게시물 URL을 찾았습니다.")
    return all_post_urls

def download_naver_blog_content(url, save_folder):
    """네이버 블로그 게시물 내용을 다운로드하여 저장"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = None
        title_selectors = [
            'h3.se_textarea', 
            'div.se-title-text',
            'h3.tit_h3',
            'div.se-module-text',
            'h3.se-title',
            'title',
            'meta[property="og:title"]'
        ]
        
        for selector in title_selectors:
            title_element = soup.select_one(selector)
            if title_element:
                if selector == 'meta[property="og:title"]':
                    title = title_element.get('content', '').strip()
                else:
                    title = title_element.get_text().strip()
                break
        
        if not title:
            log_no_match = re.search(r'logNo=(\d+)', url)
            if log_no_match:
                title = f"네이버블로그_게시물_{log_no_match.group(1)}"
            else:
                title = f"네이버블로그_게시물_{int(time.time())}"
        
        clean_title = re.sub(r'[\\/*?:"<>|]', "", title)
        clean_title = clean_title.replace('\n', '').replace('\r', '').strip()
        
        if len(clean_title) > 50:
            clean_title = clean_title[:50]
        
        game_name = clean_title
        patterns = [
            r'^(.*?)\s*(?:하는\s*법|방법|규칙|설명서|게임방법|플레이\s*방법)',
            r'^(.*?)\s*보드게임',
            r'^보드게임\s*(.*?)\s*'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, clean_title)
            if match:
                extracted = match.group(1).strip()
                if extracted:  # 빈 문자열이 아닌 경우만
                    game_name = extracted
                    break
        
        # 내용 추출
        content_selectors = [
            'div.se-main-container',
            'div.post_ct',
            '.se_component_wrap',
            '.se-module-text',
            '.view',
            '#viewTypeSelector',
            '.post-view'
        ]
        
        content_text = None
        for selector in content_selectors:
            content = soup.select_one(selector)
            if content:
                content_text = content.get_text().strip()
                break
        
        if not content_text:
            body = soup.select_one('body')
            if body:
                content_text = body.get_text().strip()
            else:
                content_text = "내용을 추출할 수 없습니다."
        
        base_save_path = os.path.join(save_folder, f"{game_name}")
        save_path = f"{base_save_path}.txt"
        
        counter = 1
        while os.path.exists(save_path):
            save_path = f"{base_save_path}_{counter}.txt"
            counter += 1
        
        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(content_text)
            
        print(f"게시물 '{game_name}'의 내용을 저장했습니다: {save_path}")
        return True, game_name
        
    except Exception as e:
        print(f"게시물 다운로드 오류: {e}")
        print(f"URL: {url}")
        return False, None

def download_all_blog_posts(blog_list_url, save_folder):
    """블로그의 모든 게시물을 다운로드하는 메인 함수"""
    os.makedirs(save_folder, exist_ok=True)
    
    post_urls = get_all_post_urls(blog_list_url)
    
    if not post_urls:
        print("다운로드할 게시물이 없습니다.")
        return

    successful_downloads = 0
    failed_downloads = 0
    
    for i, url in enumerate(post_urls, 1):
        print(f"\n게시물 {i}/{len(post_urls)} 다운로드 중...")
        success, _ = download_naver_blog_content(url, save_folder)
        
        if success:
            successful_downloads += 1
        else:
            failed_downloads += 1
        
        time.sleep(random.uniform(2.0, 5.0))
    
    print("\n===== 다운로드 완료 =====")
    print(f"총 게시물: {len(post_urls)}")
    print(f"성공: {successful_downloads}")
    print(f"실패: {failed_downloads}")

if __name__ == "__main__":
    blog_list_url = "https://blog.naver.com/PostList.naver?blogId=mukjjippa_boardgame&categoryNo=6&skinType=&skinId=&from=menu&userSelectMenu=true"
    
    save_folder = os.path.expanduser("~/Desktop/data")
    
    download_all_blog_posts(blog_list_url, save_folder)