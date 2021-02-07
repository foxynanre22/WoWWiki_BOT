import requests
import io
from bs4 import BeautifulSoup
import csv
from project.Parser.ArticleModel import ArticleModel

class WoWWikiParser:

    def __init__(self, parseURL):
        self.HOST = 'https://wowwiki-archive.fandom.com/'
        self.HEADERS = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.344'}

        self.HTML = requests.get(parseURL, headers=self.HEADERS, params='').text
        self.soup = BeautifulSoup(self.HTML, 'html.parser')
        self.parseCategory = parseURL[50:]

    def SaveToDatabase(self, members, DBContext):
        for member in members:
            DBContext.add_article(member)


    #общая функция парсинга. сначала берет ссылки, потом по ним находит инфу/картинку и делает members - как завершенный сборник данных
    async def GetParsedData(self):
        member_links = self.MemberLinks()
        members = []
        for member in member_links:
            memberInfo = self.GetMemberInfo(member['Link'])
            a = ArticleModel(member['Member Name'], member['Link'], memberInfo['Image'], memberInfo['Data'], self.parseCategory)
            members.append(a)

        return members


    #парсит страницу категорий и возвращает список, внутри которого словари. каждый словарь имеет имя объекта и ссылку на статью с ним
    def MemberLinks(self):
        dirty_links = self.soup.find_all('a', class_='category-page__member-link')
        clean_links = []

        for link in dirty_links:
            clean_links.append({
                'Member Name': link.get_text(),
                'Link': self.HOST + link.get('href')
            })

        for link in clean_links:
            if 'Category' in link['Member Name']:
                clean_links.remove(link)
        for link in clean_links:
            if 'Category' in link['Member Name']:
                clean_links.remove(link)

        return clean_links

    # хапает краткое содержание и картинку, возвращая их словарем
    def GetMemberInfo(self, memberUrl):
        memberHTML = requests.get(memberUrl, headers=self.HEADERS, params='').text
        memberSoup = BeautifulSoup(memberHTML, 'html.parser')

        memberImage = memberSoup.find('figure').find('a')
        if memberImage is not None:
            memberImage = memberImage.get('href')
        else:
            memberImage = 'NONE_IMAGE_HERE'

        memberData = memberSoup.find('div', class_='mw-parser-output')
        if memberData is not None:
            memberData = memberData.findChildren('p') #в дату запихивает все абзацы которые ток есть в parser-output
            for p in memberData:
                if len(p.get_text(strip=True)) > 100: #смотрит на длину каждого абзаца, чтобы с большей вероятностью найти вступительный
                    memberData = p.get_text(strip=True)
        else:
            memberData = 'NONE_DATA_HERE'

        memberInfo = {'Image': memberImage, 'Data':memberData}
        return memberInfo