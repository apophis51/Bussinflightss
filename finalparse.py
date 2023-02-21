import re
import openpyxl
import openai
import time
string = r"""make a 4 paragraph blog about cheap flights from houston to poland --first h2:How much are cheap flights from houston to poland --next h2: How long are cheap flights from houston to poland ( Use (11h4min)) next h2: What’s the cheapest day for cheap flights from houston to poland (use Tuseday) --next h2: How far are the cheap flights from houston to poland ( Use 5,588.21) miles --start every new question with '*' --separate the questions on its own line --make an introduction about cheap flights from houston to poland --
make a 4 paragraph blog about flights from honolulu to poland --first h2:How much are flights from honolulu to poland --next h2: How long are flights from honolulu to poland ( Use (14h25min)) next h2: What’s the cheapest day for flights from honolulu to poland (use Tuseday) --next h2: How far are the flights from honolulu to poland ( Use 7,352.10) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from honolulu to poland --
make a 4 paragraph blog about cheap flights to poland from hartford ct --first h2:How much are cheap flights to poland from hartford ct --next h2: How long are cheap flights to poland from hartford ct ( Use (8h21min)) next h2: What’s the cheapest day for cheap flights to poland from hartford ct (use Tuseday) --next h2: How far are the cheap flights to poland from hartford ct ( Use 4,149.76) miles --start every new question with '*' --separate the questions on its own line --make an introduction about cheap flights to poland from hartford ct --
make a 4 paragraph blog about glasgow to poland flights --first h2:How much are glasgow to poland flights --next h2: How long are glasgow to poland flights ( Use (2h27min)) next h2: What’s the cheapest day for glasgow to poland flights (use Tuseday) --next h2: How far are the glasgow to poland flights ( Use 1,032.22) miles --start every new question with '*' --separate the questions on its own line --make an introduction about glasgow to poland flights --
make a 4 paragraph blog about germany to poland flights --first h2:How much are germany to poland flights --next h2: How long are germany to poland flights ( Use (1h19min)) next h2: What’s the cheapest day for germany to poland flights (use Tuseday) --next h2: How far are the germany to poland flights ( Use 438.04) miles --start every new question with '*' --separate the questions on its own line --make an introduction about germany to poland flights --
make a 4 paragraph blog about flights from geneva to poland --first h2:How much are flights from geneva to poland --next h2: How long are flights from geneva to poland ( Use (1h58min)) next h2: What’s the cheapest day for flights from geneva to poland (use Tuseday) --next h2: How far are the flights from geneva to poland ( Use 782.66) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from geneva to poland --
make a 4 paragraph blog about cheap flights from gatwick to poland --first h2:How much are cheap flights from gatwick to poland --next h2: How long are cheap flights from gatwick to poland ( Use (9h39min)) next h2: What’s the cheapest day for cheap flights from gatwick to poland (use Tuseday) --next h2: How far are the cheap flights from gatwick to poland ( Use 4,839.37) miles --start every new question with '*' --separate the questions on its own line --make an introduction about cheap flights from gatwick to poland --
make a 4 paragraph blog about flights from florida to poland --first h2:How much are flights from florida to poland --next h2: How long are flights from florida to poland ( Use (10h21min)) next h2: What’s the cheapest day for flights from florida to poland (use Tuseday) --next h2: How far are the flights from florida to poland ( Use 5,210.77) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from florida to poland --
make a 4 paragraph blog about flights usa to poland --first h2:How much are flights usa to poland --next h2: How long are flights usa to poland ( Use (10h10min)) next h2: What’s the cheapest day for flights usa to poland (use Tuseday) --next h2: How far are the flights usa to poland ( Use 5,113.38) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights usa to poland --
make a 4 paragraph blog about flights from england to poland --first h2:How much are flights from england to poland --next h2: How long are flights from england to poland ( Use (10h21min)) next h2: What’s the cheapest day for flights from england to poland (use Tuseday) --next h2: How far are the flights from england to poland ( Use 5,204.16) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from england to poland --
make a 4 paragraph blog about eindhoven to poland flights --first h2:How much are eindhoven to poland flights --next h2: How long are eindhoven to poland flights ( Use (1h43min)) next h2: What’s the cheapest day for eindhoven to poland flights (use Tuseday) --next h2: How far are the eindhoven to poland flights ( Use 650.91) miles --start every new question with '*' --separate the questions on its own line --make an introduction about eindhoven to poland flights --
make a 4 paragraph blog about edinburgh to poland direct flights --first h2:How much are edinburgh to poland direct flights --next h2: How long are edinburgh to poland direct flights ( Use (2h22min)) next h2: What’s the cheapest day for edinburgh to poland direct flights (use Tuseday) --next h2: How far are the edinburgh to poland direct flights ( Use 991.08) miles --start every new question with '*' --separate the questions on its own line --make an introduction about edinburgh to poland direct flights --
make a 4 paragraph blog about flights ecuador to poland --first h2:How much are flights ecuador to poland --next h2: How long are flights ecuador to poland ( Use (13h6min)) next h2: What’s the cheapest day for flights ecuador to poland (use Tuseday) --next h2: How far are the flights ecuador to poland ( Use 6,662.15) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights ecuador to poland --
make a 4 paragraph blog about flights from east haven to poland --first h2:How much are flights from east haven to poland --next h2: How long are flights from east haven to poland ( Use (8h24min)) next h2: What’s the cheapest day for flights from east haven to poland (use Tuseday) --next h2: How far are the flights from east haven to poland ( Use 4,180.40) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from east haven to poland --
make a 4 paragraph blog about flights from dublin to poland --first h2:How much are flights from dublin to poland --next h2: How long are flights from dublin to poland ( Use (2h37min)) next h2: What’s the cheapest day for flights from dublin to poland (use Tuseday) --next h2: How far are the flights from dublin to poland ( Use 1,120.66) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from dublin to poland --
make a 4 paragraph blog about cheap flights from dubai to poland --first h2:How much are cheap flights from dubai to poland --next h2: How long are cheap flights from dubai to poland ( Use (5h25min)) next h2: What’s the cheapest day for cheap flights from dubai to poland (use Tuseday) --next h2: How far are the cheap flights from dubai to poland ( Use 2,601.92) miles --start every new question with '*' --separate the questions on its own line --make an introduction about cheap flights from dubai to poland --
make a 4 paragraph blog about flights from doncaster to poland --first h2:How much are flights from doncaster to poland --next h2: How long are flights from doncaster to poland ( Use (2h13min)) next h2: What’s the cheapest day for flights from doncaster to poland (use Tuseday) --next h2: How far are the flights from doncaster to poland ( Use 908.54) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from doncaster to poland --
make a 4 paragraph blog about detroit dtw to poland flights --first h2:How much are detroit dtw to poland flights --next h2: How long are detroit dtw to poland flights ( Use (8h59min)) next h2: What’s the cheapest day for detroit dtw to poland flights (use Tuseday) --next h2: How far are the detroit dtw to poland flights ( Use 4,483.55) miles --start every new question with '*' --separate the questions on its own line --make an introduction about detroit dtw to poland flights --
make a 4 paragraph blog about flights from des moines ia to poland --first h2:How much are flights from des moines ia to poland --next h2: How long are flights from des moines ia to poland ( Use (9h42min)) next h2: What’s the cheapest day for flights from des moines ia to poland (use Tuseday) --next h2: How far are the flights from des moines ia to poland ( Use 4,862.21) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from des moines ia to poland --
make a 4 paragraph blog about cheap flights denver to poland --first h2:How much are cheap flights denver to poland --next h2: How long are cheap flights denver to poland ( Use (10h31min)) next h2: What’s the cheapest day for cheap flights denver to poland (use Tuseday) --next h2: How far are the cheap flights denver to poland ( Use 5,298.39) miles --start every new question with '*' --separate the questions on its own line --make an introduction about cheap flights denver to poland --
make a 4 paragraph blog about flights from delhi to poland --first h2:How much are flights from delhi to poland --next h2: How long are flights from delhi to poland ( Use (6h44min)) next h2: What’s the cheapest day for flights from delhi to poland (use Tuseday) --next h2: How far are the flights from delhi to poland ( Use 3,292.25) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from delhi to poland --
make a 4 paragraph blog about buffalo ny katowice poland flights december --first h2:How much are buffalo ny katowice poland flights december --next h2: How long are buffalo ny katowice poland flights december ( Use (7h23min)) next h2: What’s the cheapest day for buffalo ny katowice poland flights december (use Tuseday) --next h2: How far are the buffalo ny katowice poland flights december ( Use 3,640.71) miles --start every new question with '*' --separate the questions on its own line --make an introduction about buffalo ny katowice poland flights december --
make a 4 paragraph blog about flights from dc to poland --first h2:How much are flights from dc to poland --next h2: How long are flights from dc to poland ( Use (8h55min)) next h2: What’s the cheapest day for flights from dc to poland (use Tuseday) --next h2: How far are the flights from dc to poland ( Use 4,448.94) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from dc to poland --
make a 4 paragraph blog about flights to poland from dallas --first h2:How much are flights to poland from dallas --next h2: How long are flights to poland from dallas ( Use (10h50min)) next h2: What’s the cheapest day for flights to poland from dallas (use Tuseday) --next h2: How far are the flights to poland from dallas ( Use 5,459.84) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights to poland from dallas --
make a 4 paragraph blog about flights cork to poland --first h2:How much are flights cork to poland --next h2: How long are flights cork to poland ( Use (2h49min)) next h2: What’s the cheapest day for flights cork to poland (use Tuseday) --next h2: How far are the flights cork to poland ( Use 1,230.45) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights cork to poland --
make a 4 paragraph blog about copenhagen to poland flights --first h2:How much are copenhagen to poland flights --next h2: How long are copenhagen to poland flights ( Use (1h15min)) next h2: What’s the cheapest day for copenhagen to poland flights (use Tuseday) --next h2: How far are the copenhagen to poland flights ( Use 397.08) miles --start every new question with '*' --separate the questions on its own line --make an introduction about copenhagen to poland flights --
make a 4 paragraph blog about flights from chicago to poland cost --first h2:How much are flights from chicago to poland cost --next h2: How long are flights from chicago to poland cost ( Use (9h19min)) next h2: What’s the cheapest day for flights from chicago to poland cost (use Tuseday) --next h2: How far are the flights from chicago to poland cost ( Use 4,660.83) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from chicago to poland cost --
make a 4 paragraph blog about flights to poland from charlotte, nc --first h2:How much are flights to poland from charlotte, nc --next h2: How long are flights to poland from charlotte, nc ( Use (9h33min)) next h2: What’s the cheapest day for flights to poland from charlotte, nc (use Tuseday) --next h2: How far are the flights to poland from charlotte, nc ( Use 4,780.23) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights to poland from charlotte, nc --
make a 4 paragraph blog about flights to poland from cardiff --first h2:How much are flights to poland from cardiff --next h2: How long are flights to poland from cardiff ( Use (2h25min)) next h2: What’s the cheapest day for flights to poland from cardiff (use Tuseday) --next h2: How far are the flights to poland from cardiff ( Use 1,015.37) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights to poland from cardiff --
make a 4 paragraph blog about canncun to poland flights --first h2:How much are canncun to poland flights --next h2: How long are canncun to poland flights ( Use (11h25min)) next h2: What’s the cheapest day for canncun to poland flights (use Tuseday) --next h2: How far are the canncun to poland flights ( Use 5,770.57) miles --start every new question with '*' --separate the questions on its own line --make an introduction about canncun to poland flights --
make a 4 paragraph blog about cheap flights from canada to poland --first h2:How much are cheap flights from canada to poland --next h2: How long are cheap flights from canada to poland ( Use (8h35min)) next h2: What’s the cheapest day for cheap flights from canada to poland (use Tuseday) --next h2: How far are the cheap flights from canada to poland ( Use 4,272.12) miles --start every new question with '*' --separate the questions on its own line --make an introduction about cheap flights from canada to poland --
make a 4 paragraph blog about flights from ca to poland --first h2:How much are flights from ca to poland --next h2: How long are flights from ca to poland ( Use (11h32min)) next h2: What’s the cheapest day for flights from ca to poland (use Tuseday) --next h2: How far are the flights from ca to poland ( Use 5,835.14) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from ca to poland --
make a 4 paragraph blog about direct flights from bulgaria to poland --first h2:How much are direct flights from bulgaria to poland --next h2: How long are direct flights from bulgaria to poland ( Use (1h50min)) next h2: What’s the cheapest day for direct flights from bulgaria to poland (use Tuseday) --next h2: How far are the direct flights from bulgaria to poland ( Use 708.96) miles --start every new question with '*' --separate the questions on its own line --make an introduction about direct flights from bulgaria to poland --
make a 4 paragraph blog about cheap flights from brussels to poland --first h2:How much are cheap flights from brussels to poland --next h2: How long are cheap flights from brussels to poland ( Use (1h50min)) next h2: What’s the cheapest day for cheap flights from brussels to poland (use Tuseday) --next h2: How far are the cheap flights from brussels to poland ( Use 708.06) miles --start every new question with '*' --separate the questions on its own line --make an introduction about cheap flights from brussels to poland --
make a 4 paragraph blog about bristol to poland cheap flights --first h2:How much are bristol to poland cheap flights --next h2: How long are bristol to poland cheap flights ( Use (2h22min)) next h2: What’s the cheapest day for bristol to poland cheap flights (use Tuseday) --next h2: How far are the bristol to poland cheap flights ( Use 991.02) miles --start every new question with '*' --separate the questions on its own line --make an introduction about bristol to poland cheap flights --
make a 4 paragraph blog about flights to poland from brisbane --first h2:How much are flights to poland from brisbane --next h2: How long are flights to poland from brisbane ( Use (18h24min)) next h2: What’s the cheapest day for flights to poland from brisbane (use Tuseday) --next h2: How far are the flights to poland from brisbane ( Use 9,455.54) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights to poland from brisbane --
make a 4 paragraph blog about flights from bournemouth to poland --first h2:How much are flights from bournemouth to poland --next h2: How long are flights from bournemouth to poland ( Use (2h20min)) next h2: What’s the cheapest day for flights from bournemouth to poland (use Tuseday) --next h2: How far are the flights from bournemouth to poland ( Use 973.61) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from bournemouth to poland --
make a 4 paragraph blog about cheap flights to poland from boston --first h2:How much are cheap flights to poland from boston --next h2: How long are cheap flights to poland from boston ( Use (8h11min)) next h2: What’s the cheapest day for cheap flights to poland from boston (use Tuseday) --next h2: How far are the cheap flights to poland from boston ( Use 4,061.56) miles --start every new question with '*' --separate the questions on its own line --make an introduction about cheap flights to poland from boston --
make a 4 paragraph blog about flights to poland from birmingham --first h2:How much are flights to poland from birmingham --next h2: How long are flights to poland from birmingham ( Use (10h7min)) next h2: What’s the cheapest day for flights to poland from birmingham (use Tuseday) --next h2: How far are the flights to poland from birmingham ( Use 5,084.51) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights to poland from birmingham --
make a 4 paragraph blog about flights txl to bydgoszcz poland --first h2:How much are flights txl to bydgoszcz poland --next h2: How long are flights txl to bydgoszcz poland ( Use (1h4min)) next h2: What’s the cheapest day for flights txl to bydgoszcz poland (use Tuseday) --next h2: How far are the flights txl to bydgoszcz poland ( Use 305.53) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights txl to bydgoszcz poland --
make a 4 paragraph blog about belfast to poland flights --first h2:How much are belfast to poland flights --next h2: How long are belfast to poland flights ( Use (2h34min)) next h2: What’s the cheapest day for belfast to poland flights (use Tuseday) --next h2: How far are the belfast to poland flights ( Use 1,098.71) miles --start every new question with '*' --separate the questions on its own line --make an introduction about belfast to poland flights --
make a 4 paragraph blog about flights to poland from bdl --first h2:How much are flights to poland from bdl --next h2: How long are flights to poland from bdl ( Use (8h20min)) next h2: What’s the cheapest day for flights to poland from bdl (use Tuseday) --next h2: How far are the flights to poland from bdl ( Use 4,141.09) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights to poland from bdl --
make a 4 paragraph blog about flights from barcelona to poland --first h2:How much are flights from barcelona to poland --next h2: How long are flights from barcelona to poland ( Use (2h41min)) next h2: What’s the cheapest day for flights from barcelona to poland (use Tuseday) --next h2: How far are the flights from barcelona to poland ( Use 1,155.46) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from barcelona to poland --
make a 4 paragraph blog about flights bangkok to poland --first h2:How much are flights bangkok to poland --next h2: How long are flights bangkok to poland ( Use (10h3min)) next h2: What’s the cheapest day for flights bangkok to poland (use Tuseday) --next h2: How far are the flights bangkok to poland ( Use 5,046.53) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights bangkok to poland --
make a 4 paragraph blog about flights from bwi to poland --first h2:How much are flights from bwi to poland --next h2: How long are flights from bwi to poland ( Use (8h51min)) next h2: What’s the cheapest day for flights from bwi to poland (use Tuseday) --next h2: How far are the flights from bwi to poland ( Use 4,415.85) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from bwi to poland --
make a 4 paragraph blog about australia to poland flights --first h2:How much are australia to poland flights --next h2: How long are australia to poland flights ( Use (16h44min)) next h2: What’s the cheapest day for australia to poland flights (use Tuseday) --next h2: How far are the australia to poland flights ( Use 8,580.12) miles --start every new question with '*' --separate the questions on its own line --make an introduction about australia to poland flights --
make a 4 paragraph blog about from austin to poland cheap flights --first h2:How much are from austin to poland cheap flights --next h2: How long are from austin to poland cheap flights ( Use (11h10min)) next h2: What’s the cheapest day for from austin to poland cheap flights (use Tuseday) --next h2: How far are the from austin to poland cheap flights ( Use 5,637.51) miles --start every new question with '*' --separate the questions on its own line --make an introduction about from austin to poland cheap flights --
make a 4 paragraph blog about flights from atl to poland --first h2:How much are flights from atl to poland --next h2: How long are flights from atl to poland ( Use (9h56min)) next h2: What’s the cheapest day for flights from atl to poland (use Tuseday) --next h2: How far are the flights from atl to poland ( Use 4,986.74) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from atl to poland --
make a 4 paragraph blog about flights from arlanda to poland --first h2:How much are flights from arlanda to poland --next h2: How long are flights from arlanda to poland ( Use (1h27min)) next h2: What’s the cheapest day for flights from arlanda to poland (use Tuseday) --next h2: How far are the flights from arlanda to poland ( Use 508.64) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from arlanda to poland --
make a 4 paragraph blog about antigua to poland flights --first h2:How much are antigua to poland flights --next h2: How long are antigua to poland flights ( Use (9h55min)) next h2: What’s the cheapest day for antigua to poland flights (use Tuseday) --next h2: How far are the antigua to poland flights ( Use 4,979.64) miles --start every new question with '*' --separate the questions on its own line --make an introduction about antigua to poland flights --
make a 4 paragraph blog about flights from albuquerque to poland --first h2:How much are flights from albuquerque to poland --next h2: How long are flights from albuquerque to poland ( Use (11h8min)) next h2: What’s the cheapest day for flights from albuquerque to poland (use Tuseday) --next h2: How far are the flights from albuquerque to poland ( Use 5,622.21) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights from albuquerque to poland --
make a 4 paragraph blog about flights to poland from uk --first h2:How much are flights to poland from uk --next h2: How long are flights to poland from uk ( Use (2h20min)) next h2: What’s the cheapest day for flights to poland from uk (use Tuseday) --next h2: How far are the flights to poland from uk ( Use 968.79) miles --start every new question with '*' --separate the questions on its own line --make an introduction about flights to poland from uk --

	





"""
text = open("gpt3.txt", "w")
for x in string.rsplit("--"):
    print(x )
    text.writelines(x)
 
