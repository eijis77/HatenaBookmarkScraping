# coding:utf-8
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

url_list = [
    # urlの配列
    '',
    '',
    ''
]
# ブラウザを開く。
browse = webdriver.Chrome(executable_path='/Users/Macのユーザー名/chromedriver')

# newspicksのトップページ
browse.get('はてなブックマークのログインページURL')
# 2秒待ちます
time.sleep(2)

# メールアドレス入力
email = browse.find_element_by_id('login-name')
email.click()
email.send_keys('はてなIDまたはメールアドレス')

# パスワード入力
password = browse.find_element_by_class_name('password')
password.click()
password.send_keys('パスワード')

# ログインボタンクリック
button_username = browse.find_element_by_class_name('submit-button')
button_username.click()

time.sleep(8)

for url in url_list:

    time.sleep(4)

    pick_button = browse.find_element_by_class_name("add")
    pick_button.click()

    time.sleep(2)

    text_field1 = browse.find_element_by_class_name("js-add-bookmark-url-form-url-textbox")
    text_field1.send_keys(url)

    register_button = browse.find_element_by_class_name("js-bookmark-add-url-form-submit")
    register_button.click()
    time.sleep(5)
    try:
        check_button = browse.find_element_by_class_name("entry-notFound-btn")
        check_button.click()
        time.sleep(3)
        submit_button = browse.find_element_by_class_name("js-bookmarkadd-submit-btn")
        submit_button.click()
    except:
        # 存在しない時の処理
        submit_button = browse.find_element_by_class_name("js-bookmarkadd-submit-btn")
        submit_button.click()

    time.sleep(5)
