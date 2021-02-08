import requests
from bs4 import BeautifulSoup
from project.WoWWiki_BOT.Parser.ArticleModel import ArticleModel


class WoWWikiParser:
    """
    A class to represent a parser.

    ...

    Attributes
    ----------
    HOST : str
        constant that contain host of WoW wiki fandom
    HEADERS : dict
        dictionary with headers for the requests to the WoW wiki portal
    HTML : str
        parsing html document in string format
    soup : BeautifulSoup
        represents the html document as a nested data structure
    parseCategory : str
        contain a name of the category that parsing by this parser

    Methods
    -------
    SaveToDatabase(members, DBContext):
        add or update information about article to the database
    GetParsedData():
        method that parses articles by category of the parser
    MemberLinks():
        method that grab links and names of the articles
    GetMemberInfo(memberUrl):
        method that grab description and image of the article
    """

    def __init__(self, parseURL):
        """
        Constructs all the necessary attributes for the parser object.

        Parameters
        ----------
            parseURL : str
                url to the category page of wowwiki-archive.fandom.com
                ex.: https://wowwiki-archive.fandom.com/wiki/Category:Classes
        """

        self.HOST = "https://wowwiki-archive.fandom.com/"
        self.HEADERS = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                      "image/avif,image/webp,image/apng,*/*;q=0.8,application"
                      "/signed-exchange;v=b3;q=0.9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/87.0.4280.141 Safari/537.36 "
                          "OPR/73.0.3856.344",
        }

        self.HTML = requests.get(parseURL,
                                 headers=self.HEADERS, params="").text
        self.soup = BeautifulSoup(self.HTML, "html.parser")
        self.parseCategory = parseURL[49:]

    def SaveToDatabase(self, members, DBContext):
        """
        add article that database doesnt contain and update
        information about article where it contains in database
        """
        for member in members:
            is_contain = DBContext.find_article(member.name.lower())

            if is_contain:
                DBContext.update_article(member)
            else:
                DBContext.add_article(member)

    async def GetParsedData(self):
        """
        return a list that contains objects with type Article.
        do it with MemberLinks() and GetMemberInfo()
        """
        member_links = self.MemberLinks()
        members = []
        for member in member_links:
            memberInfo = self.GetMemberInfo(member["Link"])
            a = ArticleModel(
                member["Member Name"],
                member["Link"],
                memberInfo["Image"],
                memberInfo["Data"],
                self.parseCategory,
            )
            members.append(a)

        return members

    def MemberLinks(self):
        """
        return a list of dictionaries.
        every dictionary contains name of article and link to it
        """
        dirty_links = self.soup.find_all("a",
                                         class_="category-page__member-link")
        clean_links = []

        for link in dirty_links:
            clean_links.append(
                {"Member Name": link.get_text(),
                 "Link": self.HOST + link.get("href")}
            )

        # clean list from trash links before return
        for link in clean_links:
            if "Category" in link["Member Name"]:
                clean_links.remove(link)
        for link in clean_links:
            if "Category" in link["Member Name"]:
                clean_links.remove(link)

        return clean_links

    def GetMemberInfo(self, memberUrl):
        """
        return a dictionary that contain a part
        of the article and photo which are on the url
        """
        memberHTML = requests.get(memberUrl,
                                  headers=self.HEADERS, params="").text
        memberSoup = BeautifulSoup(memberHTML, "html.parser")

        memberImage = memberSoup.find("figure").find("a")
        if memberImage is not None:
            memberImage = memberImage.get("href")
        else:
            memberImage = "NONE_IMAGE_HERE"

        memberData = memberSoup.find("div", class_="mw-parser-output")
        if memberData is not None:
            memberData = memberData.findChildren(
                "p"
            )  # grab all <p> tags from <div> with class "mw-parser-output"
            for p in memberData:
                if (
                    len(p.get_text(strip=True)) > 100
                ):  # grab first large, significant text
                    memberData = p.get_text(strip=True)
                    break
        else:
            memberData = "NONE_DATA_HERE"

        memberInfo = {"Image": memberImage, "Data": memberData}
        return memberInfo
