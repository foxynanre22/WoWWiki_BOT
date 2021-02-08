import logging

from project.WoWWiki_BOT.Parser.Parser import WoWWikiParser

"""Set up logging"""
logging.basicConfig(
    level=logging.DEBUG,
    format="{asctime} {levelname:<8} {message}",
    style='{',
    filename='%slog' % __file__[:-2],
    filemode='w'
)

"""Initialization Main Categories Parcers"""
RaceParser = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Races"
)
HordeParser = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Horde"
)
AllianceParser = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Alliance"
)
ClassesParser = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Classes"
)
"""Initialization Alliance Categories Parcers"""
AllianceParser1 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Companions"
)
AllianceParser2 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/"
    "Category:Alliance-only_achievements"
)
AllianceParser3 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Blacksmithing_trainers"
)
AllianceParser4 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Companion_vendors"
)
AllianceParser5 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Alliance_territories"
)
AllianceParser6 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Alliance_factions"
)
"""Initialization Horde Categories Parcers"""
HordeParser1 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Armor_vendors"
)
HordeParser2 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Portal_trainers"
)
HordeParser3 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Quests_at_15"
)
HordeParser4 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Horde_factions"
)
HordeParser5 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Stable_masters"
)
HordeParser6 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Horde_territories"
)
HordeParser7 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Horde-only_achievements"
)
"""Initialization Classes Categories Parcers"""
ClassesParser1 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Priests"
)
ClassesParser2 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Rogues"
)
ClassesParser3 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Mages"
)
ClassesParser4 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Shamans"
)
ClassesParser5 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Death_knights"
)
ClassesParser6 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Druids"
)
ClassesParser7 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Warlocks"
)
ClassesParser8 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Warriors"
)
ClassesParser9 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Hunters"
)
"""Initialization Race Categories Parcers"""
RaceParser1 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Racial_traits"
)
RaceParser2 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Jungle_trolls"
)
RaceParser3 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Ancients"
)
RaceParser4 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Murlocs"
)
RaceParser5 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Naga"
)
RaceParser6 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Blood_elves"
)
RaceParser7 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Night_elves"
)
RaceParser8 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Orcs"
)
RaceParser9 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Draenei"
)
RaceParser10 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Pandaren"
)
RaceParser11 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Dwarves"
)
RaceParser12 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Eredar"
)
RaceParser13 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Forsaken"
)
RaceParser14 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Ghouls"
)
RaceParser15 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Gnomes"
)
RaceParser16 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Goblins"
)
RaceParser17 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Taunka"
)
RaceParser18 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Tauren"
)
RaceParser19 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Trolls"
)
RaceParser20 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Vrykul"
)
RaceParser21 = WoWWikiParser(
    "https://wowwiki-archive.fandom.com/wiki/Category:Humans"
)


async def ParseAndSaveAlliance(database):
    """
    parse all categories about Alliance
    :param database:
    :return bool:
    """
    # parsing
    AllianceData = await AllianceParser.GetParsedData()
    logging.debug("Alliance was parced successfully.")
    AllianceData1 = await AllianceParser1.GetParsedData()
    logging.debug("Alliance 1 was parced successfully.")
    AllianceData2 = await AllianceParser2.GetParsedData()
    logging.debug("Alliance 2 was parced successfully.")
    AllianceData3 = await AllianceParser3.GetParsedData()
    logging.debug("Alliance 3 was parced successfully.")
    AllianceData4 = await AllianceParser4.GetParsedData()
    logging.debug("Alliance 4 was parced successfully.")
    AllianceData5 = await AllianceParser5.GetParsedData()
    logging.debug("Alliance 5 was parced successfully.")
    AllianceData6 = await AllianceParser6.GetParsedData()
    logging.debug("Alliance 6 was parced successfully.")

    # save to database
    AllianceParser.SaveToDatabase(AllianceData, database)
    logging.debug("Alliance was saved to the database successfully.")
    AllianceParser1.SaveToDatabase(AllianceData1, database)
    logging.debug("Alliance 1 was saved to the database successfully.")
    AllianceParser2.SaveToDatabase(AllianceData2, database)
    logging.debug("Alliance 2 was saved to the database successfully.")
    AllianceParser3.SaveToDatabase(AllianceData3, database)
    logging.debug("Alliance 3 was saved to the database successfully.")
    AllianceParser4.SaveToDatabase(AllianceData4, database)
    logging.debug("Alliance 4 was saved to the database successfully.")
    AllianceParser5.SaveToDatabase(AllianceData5, database)
    logging.debug("Alliance 5 was saved to the database successfully.")
    AllianceParser6.SaveToDatabase(AllianceData6, database)
    logging.debug("Alliance 6 was saved to the database successfully.")

    return True


async def ParseAndSaveHorde(database):
    """
    parse all categories about Horde
    :param database:
    :return bool:
    """
    # parsing
    HordeData = await HordeParser.GetParsedData()
    logging.debug("Horde was parced successfully.")
    HordeData1 = await HordeParser1.GetParsedData()
    logging.debug("Horde 1 was parced successfully.")
    HordeData2 = await HordeParser2.GetParsedData()
    logging.debug("Horde 2 was parced successfully.")
    HordeData3 = await HordeParser3.GetParsedData()
    logging.debug("Horde 3 was parced successfully.")
    HordeData4 = await HordeParser4.GetParsedData()
    logging.debug("Horde 4 was parced successfully.")
    HordeData5 = await HordeParser5.GetParsedData()
    logging.debug("Horde 5 was parced successfully.")
    HordeData6 = await HordeParser6.GetParsedData()
    logging.debug("Horde 6 was parced successfully.")
    HordeData7 = await HordeParser7.GetParsedData()
    logging.debug("Horde 7 was parced successfully.")

    # save to database
    HordeParser.SaveToDatabase(HordeData, database)
    logging.debug("Horde was saved to the database successfully.")
    HordeParser1.SaveToDatabase(HordeData1, database)
    logging.debug("Horde 1 was saved to the database successfully.")
    HordeParser2.SaveToDatabase(HordeData2, database)
    logging.debug("Horde 2 was saved to the database successfully.")
    HordeParser3.SaveToDatabase(HordeData3, database)
    logging.debug("Horde 3 was saved to the database successfully.")
    HordeParser4.SaveToDatabase(HordeData4, database)
    logging.debug("Horde 4 was saved to the database successfully.")
    HordeParser5.SaveToDatabase(HordeData5, database)
    logging.debug("Horde 5 was saved to the database successfully.")
    HordeParser6.SaveToDatabase(HordeData6, database)
    logging.debug("Horde 6 was saved to the database successfully.")
    HordeParser7.SaveToDatabase(HordeData7, database)
    logging.debug("Horde 7 was saved to the database successfully.")

    return True


async def ParseAndSaveClasses(database):
    """
    parse all categories about Classes
    :param database:
    :return bool:
    """
    # parsing
    ClassesData = await ClassesParser.GetParsedData()
    logging.debug("Classes was parced successfully.")
    ClassesData1 = await ClassesParser1.GetParsedData()
    logging.debug("Classes 1 was parced successfully.")
    ClassesData2 = await ClassesParser2.GetParsedData()
    logging.debug("Classes 2 was parced successfully.")
    ClassesData3 = await ClassesParser3.GetParsedData()
    logging.debug("Classes 3 was parced successfully.")
    ClassesData4 = await ClassesParser4.GetParsedData()
    logging.debug("Classes 4 was parced successfully.")
    ClassesData5 = await ClassesParser5.GetParsedData()
    logging.debug("Classes 5 was parced successfully.")
    ClassesData6 = await ClassesParser6.GetParsedData()
    logging.debug("Classes 6 was parced successfully.")
    ClassesData7 = await ClassesParser7.GetParsedData()
    logging.debug("Classes 7 was parced successfully.")
    ClassesData8 = await ClassesParser8.GetParsedData()
    logging.debug("Classes 8 was parced successfully.")
    ClassesData9 = await ClassesParser9.GetParsedData()
    logging.debug("Classes 9 was parced successfully.")
    # save to database
    ClassesParser.SaveToDatabase(ClassesData, database)
    logging.debug("Classes was saved to the database successfully.")
    ClassesParser1.SaveToDatabase(ClassesData1, database)
    logging.debug("Classes 1 was saved to the database successfully.")
    ClassesParser2.SaveToDatabase(ClassesData2, database)
    logging.debug("Classes 2 was saved to the database successfully.")
    ClassesParser3.SaveToDatabase(ClassesData3, database)
    logging.debug("Classes 3 was saved to the database successfully.")
    ClassesParser4.SaveToDatabase(ClassesData4, database)
    logging.debug("Classes 4 was saved to the database successfully.")
    ClassesParser5.SaveToDatabase(ClassesData5, database)
    logging.debug("Classes 5 was saved to the database successfully.")
    ClassesParser6.SaveToDatabase(ClassesData6, database)
    logging.debug("Classes 6 was saved to the database successfully.")
    ClassesParser7.SaveToDatabase(ClassesData7, database)
    logging.debug("Classes 7 was saved to the database successfully.")
    ClassesParser8.SaveToDatabase(ClassesData8, database)
    logging.debug("Classes 8 was saved to the database successfully.")
    ClassesParser9.SaveToDatabase(ClassesData9, database)
    logging.debug("Classes 9 was saved to the database successfully.")

    return True


async def ParseAndSaveRace(database):
    """
    parse all categories about Races
    :param database:
    :return bool:
    """
    # parsing
    RaceData = await RaceParser.GetParsedData()
    logging.debug("Races was parced successfully.")
    RaceData1 = await RaceParser1.GetParsedData()
    logging.debug("Races 1 was parced successfully.")
    RaceData2 = await RaceParser2.GetParsedData()
    logging.debug("Races 2 was parced successfully.")
    RaceData3 = await RaceParser3.GetParsedData()
    logging.debug("Races 3 was parced successfully.")
    RaceData4 = await RaceParser4.GetParsedData()
    logging.debug("Races 4 was parced successfully.")
    RaceData5 = await RaceParser5.GetParsedData()
    logging.debug("Races 5 was parced successfully.")
    RaceData6 = await RaceParser6.GetParsedData()
    logging.debug("Races 6 was parced successfully.")
    RaceData7 = await RaceParser7.GetParsedData()
    logging.debug("Races 7 was parced successfully.")
    RaceData8 = await RaceParser8.GetParsedData()
    logging.debug("Races 8 was parced successfully.")
    RaceData9 = await RaceParser9.GetParsedData()
    logging.debug("Races 9 was parced successfully.")
    RaceData10 = await RaceParser10.GetParsedData()
    logging.debug("Races 10 was parced successfully.")
    RaceData11 = await RaceParser11.GetParsedData()
    logging.debug("Races 11 was parced successfully.")
    RaceData12 = await RaceParser12.GetParsedData()
    logging.debug("Races 12 was parced successfully.")
    RaceData13 = await RaceParser13.GetParsedData()
    logging.debug("Races 13 was parced successfully.")
    RaceData14 = await RaceParser14.GetParsedData()
    logging.debug("Races 14 was parced successfully.")
    RaceData15 = await RaceParser15.GetParsedData()
    logging.debug("Races 15 was parced successfully.")
    RaceData16 = await RaceParser16.GetParsedData()
    logging.debug("Races 16 was parced successfully.")
    RaceData17 = await RaceParser17.GetParsedData()
    logging.debug("Races 17 was parced successfully.")
    RaceData18 = await RaceParser18.GetParsedData()
    logging.debug("Races 18 was parced successfully.")
    RaceData19 = await RaceParser19.GetParsedData()
    logging.debug("Races 19 was parced successfully.")
    RaceData20 = await RaceParser20.GetParsedData()
    logging.debug("Races 20 was parced successfully.")
    RaceData21 = await RaceParser21.GetParsedData()
    logging.debug("Races 21 was parced successfully.")
    # save to database
    RaceParser.SaveToDatabase(RaceData, database)
    logging.debug("Races was saved to the database successfully.")
    RaceParser1.SaveToDatabase(RaceData1, database)
    logging.debug("Races 1 was saved to the database successfully.")
    RaceParser2.SaveToDatabase(RaceData2, database)
    logging.debug("Races 2 was saved to the database successfully.")
    RaceParser3.SaveToDatabase(RaceData3, database)
    logging.debug("Races 3 was saved to the database successfully.")
    RaceParser4.SaveToDatabase(RaceData4, database)
    logging.debug("Races 4 was saved to the database successfully.")
    RaceParser5.SaveToDatabase(RaceData5, database)
    logging.debug("Races 5 was saved to the database successfully.")
    RaceParser6.SaveToDatabase(RaceData6, database)
    logging.debug("Races 6 was saved to the database successfully.")
    RaceParser7.SaveToDatabase(RaceData7, database)
    logging.debug("Races 7 was saved to the database successfully.")
    RaceParser8.SaveToDatabase(RaceData8, database)
    logging.debug("Races 8 was saved to the database successfully.")
    RaceParser9.SaveToDatabase(RaceData9, database)
    logging.debug("Races 9 was saved to the database successfully.")
    RaceParser10.SaveToDatabase(RaceData10, database)
    logging.debug("Races 10 was saved to the database successfully.")
    RaceParser11.SaveToDatabase(RaceData11, database)
    logging.debug("Races 11 was saved to the database successfully.")
    RaceParser12.SaveToDatabase(RaceData12, database)
    logging.debug("Races 12 was saved to the database successfully.")
    RaceParser13.SaveToDatabase(RaceData13, database)
    logging.debug("Races 13 was saved to the database successfully.")
    RaceParser14.SaveToDatabase(RaceData14, database)
    logging.debug("Races 14 was saved to the database successfully.")
    RaceParser15.SaveToDatabase(RaceData15, database)
    logging.debug("Races 15 was saved to the database successfully.")
    RaceParser16.SaveToDatabase(RaceData16, database)
    logging.debug("Races 16 was saved to the database successfully.")
    RaceParser17.SaveToDatabase(RaceData17, database)
    logging.debug("Races 17 was saved to the database successfully.")
    RaceParser18.SaveToDatabase(RaceData18, database)
    logging.debug("Races 18 was saved to the database successfully.")
    RaceParser19.SaveToDatabase(RaceData19, database)
    logging.debug("Races 19 was saved to the database successfully.")
    RaceParser20.SaveToDatabase(RaceData20, database)
    logging.debug("Races 20 was saved to the database successfully.")
    RaceParser21.SaveToDatabase(RaceData21, database)
    logging.debug("Races 21 was saved to the database successfully.")

    return True


async def parcing(database):
    """
    run all parsing functions and monitoring their start|end
    :param database:
    """
    logging.info("Start All Parcing")

    logging.info("Start Alliance Parcing")
    alliance_result = await ParseAndSaveAlliance(database)
    logging.info("End Alliance Parcing")

    logging.info("Start Horde Parcing")
    horde_result = await ParseAndSaveHorde(database)
    logging.info("End Horde Parcing")

    logging.info("Start Classes Parcing")
    classes_result = await ParseAndSaveClasses(database)
    logging.info("End Classes Parcing")

    logging.info("Start Races Parcing")
    race_result = await ParseAndSaveRace(database)
    logging.info("End Races Parcing")

    if (alliance_result == horde_result == classes_result == race_result) \
            is True:
        logging.info(
            "End All Parcing"
            + "\n Next Parcing will be after 5 hours..."
        )
    else:
        logging.error("Error while parcing")
