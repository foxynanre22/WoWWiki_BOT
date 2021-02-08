from project.WoWWiki_BOT.Parser.Parser import WoWWikiParser
from datetime import datetime

#main parcers
RaceParser = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Races')
HordeParser = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Horde')
AllianceParser = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Alliance')
ClassesParser = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Classes')
#alliance parcers
AllianceParser1 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Companions')
AllianceParser2 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Alliance-only_achievements')
AllianceParser3 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Blacksmithing_trainers')
AllianceParser4 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Companion_vendors')
AllianceParser5 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Alliance_territories')
AllianceParser6 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Alliance_factions')
#horde parces
HordeParser1 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Armor_vendors')
HordeParser2 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Portal_trainers')
HordeParser3 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Quests_at_15')
HordeParser4 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Horde_factions')
HordeParser5 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Stable_masters')
HordeParser6 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Horde_territories')
HordeParser7 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Horde-only_achievements')
#classes parcers
ClassesParser1 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Priests')
ClassesParser2 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Rogues')
ClassesParser3 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Mages')
ClassesParser4 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Shamans')
ClassesParser5 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Death_knights')
ClassesParser6 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Druids')
ClassesParser7 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Warlocks')
ClassesParser8 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Warriors')
ClassesParser9 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Hunters')
#races parcers
RaceParser1 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Racial_traits')
RaceParser2 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Jungle_trolls')
RaceParser3 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Ancients')
RaceParser4 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Murlocs')
RaceParser5 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Naga')
RaceParser6 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Blood_elves')
RaceParser7 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Night_elves')
RaceParser8 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Orcs')
RaceParser9 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Draenei')
RaceParser10 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Pandaren')
RaceParser11 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Dwarves')
RaceParser12 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Eredar')
RaceParser13 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Forsaken')
RaceParser14 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Ghouls')
RaceParser15 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Gnomes')
RaceParser16 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Goblins')
RaceParser17 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Taunka')
RaceParser18 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Tauren')
RaceParser19 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Trolls')
RaceParser20 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Vrykul')
RaceParser21 = WoWWikiParser('https://wowwiki-archive.fandom.com/wiki/Category:Humans')


async def ParseAndSaveAlliance(database):
    #parsing
    AllianceData = await AllianceParser.GetParsedData()
    AllianceData1 = await AllianceParser1.GetParsedData()
    AllianceData2 = await AllianceParser2.GetParsedData()
    AllianceData3 = await AllianceParser3.GetParsedData()
    AllianceData4 = await AllianceParser4.GetParsedData()
    AllianceData5 = await AllianceParser5.GetParsedData()
    AllianceData6 = await AllianceParser6.GetParsedData()
    #save to database
    AllianceParser.SaveToDatabase(AllianceData, database)
    AllianceParser1.SaveToDatabase(AllianceData1, database)
    AllianceParser2.SaveToDatabase(AllianceData2, database)
    AllianceParser3.SaveToDatabase(AllianceData3, database)
    AllianceParser4.SaveToDatabase(AllianceData4, database)
    AllianceParser5.SaveToDatabase(AllianceData5, database)
    AllianceParser6.SaveToDatabase(AllianceData6, database)

    return True

async def ParseAndSaveHorde(database):
    # parsing
    HordeData = await HordeParser.GetParsedData()
    HordeData1 = await HordeParser1.GetParsedData()
    HordeData2 = await HordeParser2.GetParsedData()
    HordeData3 = await HordeParser3.GetParsedData()
    HordeData4 = await HordeParser4.GetParsedData()
    HordeData5 = await HordeParser5.GetParsedData()
    HordeData6 = await HordeParser6.GetParsedData()
    HordeData7 = await HordeParser7.GetParsedData()

    # save to database
    HordeParser.SaveToDatabase(HordeData, database)
    HordeParser1.SaveToDatabase(HordeData1, database)
    HordeParser2.SaveToDatabase(HordeData2, database)
    HordeParser3.SaveToDatabase(HordeData3, database)
    HordeParser4.SaveToDatabase(HordeData4, database)
    HordeParser5.SaveToDatabase(HordeData5, database)
    HordeParser6.SaveToDatabase(HordeData6, database)
    HordeParser7.SaveToDatabase(HordeData7, database)

    return True

async def ParseAndSaveClasses(database):
    # parsing
    ClassesData = await ClassesParser.GetParsedData()
    ClassesData1 = await ClassesParser1.GetParsedData()
    ClassesData2 = await ClassesParser2.GetParsedData()
    ClassesData3 = await ClassesParser3.GetParsedData()
    ClassesData4 = await ClassesParser4.GetParsedData()
    ClassesData5 = await ClassesParser5.GetParsedData()
    ClassesData6 = await ClassesParser6.GetParsedData()
    ClassesData7 = await ClassesParser7.GetParsedData()
    ClassesData8 = await ClassesParser8.GetParsedData()
    ClassesData9 = await ClassesParser9.GetParsedData()
    # save to database
    ClassesParser.SaveToDatabase(ClassesData, database)
    ClassesParser1.SaveToDatabase(ClassesData1, database)
    ClassesParser2.SaveToDatabase(ClassesData2, database)
    ClassesParser3.SaveToDatabase(ClassesData3, database)
    ClassesParser4.SaveToDatabase(ClassesData4, database)
    ClassesParser5.SaveToDatabase(ClassesData5, database)
    ClassesParser6.SaveToDatabase(ClassesData6, database)
    ClassesParser7.SaveToDatabase(ClassesData7, database)
    ClassesParser8.SaveToDatabase(ClassesData8, database)
    ClassesParser9.SaveToDatabase(ClassesData9, database)

    return True

async def ParseAndSaveRace(database):
    # parsing
    RaceData = await RaceParser.GetParsedData()
    RaceData1 = await RaceParser1.GetParsedData()
    RaceData2 = await RaceParser2.GetParsedData()
    RaceData3 = await RaceParser3.GetParsedData()
    RaceData4 = await RaceParser4.GetParsedData()
    RaceData5 = await RaceParser5.GetParsedData()
    RaceData6 = await RaceParser6.GetParsedData()
    RaceData7 = await RaceParser7.GetParsedData()
    RaceData8 = await RaceParser8.GetParsedData()
    RaceData9 = await RaceParser9.GetParsedData()
    RaceData10 = await RaceParser10.GetParsedData()
    RaceData11 = await RaceParser11.GetParsedData()
    RaceData12 = await RaceParser12.GetParsedData()
    RaceData13 = await RaceParser13.GetParsedData()
    RaceData14 = await RaceParser14.GetParsedData()
    RaceData15 = await RaceParser15.GetParsedData()
    RaceData16 = await RaceParser16.GetParsedData()
    RaceData17 = await RaceParser17.GetParsedData()
    RaceData18 = await RaceParser18.GetParsedData()
    RaceData19 = await RaceParser19.GetParsedData()
    RaceData20 = await RaceParser20.GetParsedData()
    RaceData21 = await RaceParser21.GetParsedData()
    # save to database
    RaceParser.SaveToDatabase(RaceData, database)
    RaceParser1.SaveToDatabase(RaceData1, database)
    RaceParser2.SaveToDatabase(RaceData2, database)
    RaceParser3.SaveToDatabase(RaceData3, database)
    RaceParser4.SaveToDatabase(RaceData4, database)
    RaceParser5.SaveToDatabase(RaceData5, database)
    RaceParser6.SaveToDatabase(RaceData6, database)
    RaceParser7.SaveToDatabase(RaceData7, database)
    RaceParser8.SaveToDatabase(RaceData8, database)
    RaceParser9.SaveToDatabase(RaceData9, database)
    RaceParser10.SaveToDatabase(RaceData10, database)
    RaceParser11.SaveToDatabase(RaceData11, database)
    RaceParser12.SaveToDatabase(RaceData12, database)
    RaceParser13.SaveToDatabase(RaceData13, database)
    RaceParser14.SaveToDatabase(RaceData14, database)
    RaceParser15.SaveToDatabase(RaceData15, database)
    RaceParser16.SaveToDatabase(RaceData16, database)
    RaceParser17.SaveToDatabase(RaceData17, database)
    RaceParser18.SaveToDatabase(RaceData18, database)
    RaceParser19.SaveToDatabase(RaceData19, database)
    RaceParser20.SaveToDatabase(RaceData20, database)
    RaceParser21.SaveToDatabase(RaceData21, database)

    return True

async def parcing(database):
    print("Start All Parcing: " + str(datetime.now()))

    print("Start Alliance Parcing: " + str(datetime.now()))
    alliance_result = await ParseAndSaveAlliance(database)
    print("End Alliance Parcing: " + str(datetime.now()))

    print("Start Horde Parcing: " + str(datetime.now()))
    horde_result = await ParseAndSaveHorde(database)
    print("End Horde Parcing: " + str(datetime.now()))

    print("Start Classes Parcing: " + str(datetime.now()))
    classes_result = await ParseAndSaveClasses(database)
    print("End Classes Parcing: " + str(datetime.now()))

    print("Start Races Parcing: " + str(datetime.now()))
    race_result = await ParseAndSaveRace(database)
    print("End Races Parcing: " + str(datetime.now()))

    if(alliance_result == horde_result == classes_result == race_result == True):
        print("End All Parcing: " + str(datetime.now()) + "\n Next Parcing will be after 5 hours...")
    else:
        print("Error while Parcing: " + str(datetime.now()) + "\n")